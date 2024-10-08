---
layout: default
title: Project Resources
nav_order: 5
---

# Project Resources
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Git Resources
![Git Cheat Sheet](/assets/images/git-cheat-sheet.png?raw=true "Git Cheat Sheet")

* [Git tutorial](https://kbroman.org/github_tutorial/)

## Web Design Resources

* Web Content Accessibility Guidelines (WCAG) 2021 Quick Reference: [https://www.w3.org/WAI/WCAG21/quickref/](https://www.w3.org/WAI/WCAG21/quickref/)
* Four basic principles: Perceivable, Operable, Understandable, Robust
* Semantic & Accessible HTML on MDN: [https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML)
* Accessible Rich Internet Applications (ARIA) Reference on MDN: [https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
Use ARIA only in cases that aren't covered by HTML 5 semantic tags. In particular, check out the tutorials section, where they demonstrate how a screen reader parses web pages.
* ANDI Free Accessibility Testing Tool: [https://www.ssa.gov/accessibility/andi/help/install.html](https://www.ssa.gov/accessibility/andi/help/install.html)
Do NOT use this as a one-stop shop to test for accessibility. In the end, you are responsible for ensuring compliance with accessibility standards. This tool only tests compliance with Section 508, a set of standards developed for federally-funded site accessibility. It does not necessarily imply compliance with WCAG or accessibility as a general concept.
* WebAIM Contrast Checker Tool: [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
This tool is great because it tells you whether you are passing WCAG contrast guidelines!
* Great Slideshow on Usability by UVA's own Professor Praphamontripong: [http://www.cs.virginia.edu/~up3f/cs4640/slides/4640meet03A-UsabilityPrinciples.pdf](http://www.cs.virginia.edu/~up3f/cs4640/slides/4640meet03A-UsabilityPrinciples.pdf)
* Here's a helpful infographic! For larger version, visit [https://webaim.org/resources/designers/](https://webaim.org/resources/designers/)

## Django Resources

* [Creating python virtual env](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [Tutorial on the basics of Django (YouTube Series)](https://www.youtube.com/watch?v=UmljXZIypDc)
* [Django generic editing views](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/)
* [Serving static images for your project](https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/)

## Heroku Resources
* [Deploying Django project to Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
* [Deploying Python / Django apps on Heroku](https://devcenter.heroku.com/articles/python-gunicorn)
* [Making Heroku automatically always do migrations whenever a new build is made](https://help.heroku.com/GDQ74SU2/django-migrations) - This fixes the "missing relation" problem on Heroku.
* [How to setup config variables so you don't have to store secret keys/API keys in GitHub](https://devcenter.heroku.com/articles/config-vars)
* [Setting up WhiteNoise to handle static files](https://whitenoise.readthedocs.io/en/stable/django.html)

### Live Demo Recordings

* [Sherriff's Demo on Getting Django and Heroku to work together from Fall 2023](https://www.cs.virginia.edu/~sherriff/cs3240/DjangoHeroku.mp4)

_Note: This recording talks about Amazon S3 as being an option for saving images, which it was for F23.  For F24, it is a requirement and the other options presented in this video do not apply to this semester._


### Deploying to Heroku

1. Create an account on Heroku at [https://signup.heroku.com](https://signup.heroku.com) using the SAME email address / account that you used for GitHub and the GitHub Student Pack.  Follow the instructions at [https://www.heroku.com/github-students](https://www.heroku.com/github-students) to make sure that your Heroku benefits are applied properly.
2. Next, ensure Heroku has access to your GitHub repos by linking your GitHub account in the Heroku settings.  Follow the instructions at [https://devcenter.heroku.com/articles/django-app-configuration](https://devcenter.heroku.com/articles/django-app-configuration) to learn how to make your project work on Heroku.  You can look at the [https://github.com/uva-cs3240-f21/Staff-Build-Example](https://github.com/uva-cs3240-f21/Staff-Build-Example) repo for some examples of how to set up some of the configuration files. There is also some info in the README file at the repo on steps for deploying.  There are several ways to do this and if you find another way online, that’s fine.
3. Once you think your project is ready, you can login at [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps) and create a new app. Under the Deploy tab, you can connect the GitHub repo for the project. This is why you have to get the project root setup correctly in Step 1! Once you connect the repo, you can scroll down to “Deploy Branch” on that same page and Heroku will clone your project and put it online! The link can be found in the Settings tab if you can't find it otherwise.


### Avoiding the macOS / psycopg2 error

Use this code at the bottom of your `settings.py` file to try/catch the import of django-heroku so it only has to work when deployed to heroku and not locally:

```
# Activate Django-Heroku.
# Use this code to avoid the psycopg2 / django-heroku error!  
# Do NOT import django-heroku above!
try:
    if 'HEROKU' in os.environ:
        import django_heroku
        django_heroku.settings(locals())
except ImportError:
    found = False
```

Another option that has worked for Sherriff (M2 MacBook Pro) _if_ you have homebrew installed:

```
brew install openssl
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
pip install psycopg2-binary
```

(Ask Sherriff if you have questions about the above terminal commands.)
