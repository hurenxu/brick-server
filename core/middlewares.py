'''
core.middlewares
---------------

middlewares to load campus, building information

if enabled, use request.campus to get campus information,
use reqeust.building to get building information,

@copyright:(c) 2013 SynergyLabs
@license:UCSD License. See License file for details.
'''
from .forms import BuildForm, CampusForm
from rest_framework.exceptions import ParseError
from django.shortcuts import get_object_or_404
from core.models import Campus, Building
from django.utils.functional import SimpleLazyObject
import json
from django.utils.deprecation import MiddlewareMixin


def _get_body_json(request):
    return json.loads(request.body_cache) if request.body_cache != '' else {}

def _get_all_params(request):
    param = _get_body_json(request)
    param.update(request.GET.dict())
    param.update(request.POST.dict())
    return param

def _get_campus(request):
    form = CampusForm(request.all_params)
    if not form.is_valid():
        raise ParseError("Invalid parameter")
    return get_object_or_404(Campus,
                             institution=form.cleaned_data['institution'],
                             name=form.cleaned_data['campus'])

def _get_building(request):
    form = BuildForm(request.all_params)
    if not form.is_valid():
        raise ParseError("Invalid parameter")
    return get_object_or_404(Building,
                             name=form.cleaned_data['building'],
                             campus__institution=form.cleaned_data['institution'],
                             campus__name=form.cleaned_data['campus'])

def get_cached_obj(request, name, func):
    cached_name = '_cached_%s' % name
    if not hasattr(request, cached_name):
        setattr(request, cached_name, func(request))
    return getattr(request, cached_name)

def get_lazy_obj(request, name, func):
    return SimpleLazyObject(lambda: get_cached_obj(request, name, func))


class BuildingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.body_cache = request.body
        request.all_params = get_lazy_obj(request, 'all_params',
                                          _get_all_params)
        request.campus = get_lazy_obj(request, 'campus',
                                      _get_campus)
        request.building = get_lazy_obj(request, 'building',
                                        _get_building)
