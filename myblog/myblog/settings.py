"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#项目根目录


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')#9^i0e8gluopzr#w_quu_t83_0m%w67mdcyw!ow18=r%j4o^t'#安全码

# SECURITY WARNING: don't run with debug turned on in production!（不要在实际生产中打开debug）
DEBUG = True

ALLOWED_HOSTS = [] #只允许外界通过该地址访问


# Application definition

INSTALLED_APPS = [#自带应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', #创建时新增
    'blog2' #创建时新增
]

MIDDLEWARE = [#中间键
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'#URL的根文件

TEMPLATES = [#模板
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',#可更改为第三方模版
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'#与wsgi相关的不管


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {#数据库
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [#密码认证
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('zh-Hans', _('Chinese')),
]
LANGUAGE_CODE = 'zh-Hans'#语言，中文 zh-hant繁体

TIME_ZONE = 'UTC'#时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)静态文件地址
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
