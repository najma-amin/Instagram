from django.http  import HttpResponse,Http404
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
