---
layout: default
title: Home
nav_order: 1
description: "CS 3240 - Software Engineering"
permalink: /
---

# CS 3240 - Fall 2024
## Software Engineering
_formerly known as Advanced Software Development Techniques_     
Our course is structured around understanding the different aspects of the software development lifecycle.  During this course, students will learn to elicit and model software requirements, choose from various design options for a solution, implement a large software system in teams using a modified Scrum methodology, perform quality assurance, and learn about ethical and professional issues, such as diversity issues, how to handle data responsibly, and software licensing.

[Online Coursepack]({{ site.data.externallinks.coursepack }}){: .btn  .btn-primary .mr-2 }
[Gradescope]({{ site.data.externallinks.gradescope }}){: .btn .btn-primary .mr-2  }
[Piazza]({{ site.data.externallinks.piazza }}){: .btn .btn-primary .mr-2  }
[Canvas]({{ site.data.externallinks.lms }}){: .btn .btn-primary .mr-2  }
[GitHub]({{ site.data.externallinks.github_organization }}){: .btn .btn-primary .mr-2  }

## Lecture and Lab Sessions
{% for section in site.data.semesterinfo.lecture_sections %} {{ section }}    
{% endfor %}   
## Staff Information

{% for professor in site.data.professors %}

__Instructor:__ {{ professor.name }}   
Office: {{ professor.office }}   
Office Hours: {{ professor.office_hours }}        
Email: [{{ professor.email }}]({{ professor.email }})   
Website: [{{ professor.website }}]({{ professor.website }})     

{% endfor %}

__Teaching Assistants:__ {% for ta in site.data.tas %} {{ ta.name }}, {% endfor %}  