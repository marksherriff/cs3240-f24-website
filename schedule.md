---
layout: default
title: Schedule
nav_order: 3
---

# Course Schedule
{: .no_toc }

1. TOC
{:toc} 

## Lecture Schedule

<table class="schedtab"><thead>
<tr>
    <th>Date</th>
    <th>Topic</th>
    <th>Due Dates</th>
    </tr>
    </thead>
    <tbody>
{% for day in site.data.lectureschedule %}
{% if day.type == 'holiday' %}
<tr class="holiday">
{% elsif day.type == 'quiz' %}
<tr class="quiz">
{% else %}
<tr>
{% endif %}
<td class="text-center sched">{{day.date}}</td>
<td class="sched">
{% if day.coursepack %}
<a href="{{day.coursepack}}">
{% endif %}
{{day.topic}}
{% if day.coursepack %}
    </a>
{% endif %}
{% if day.topic2 %}
&
{% if day.coursepack2 %}
<a href="{{day.coursepack2}}">
{% endif %}
{{day.topic2}}
{% if day.coursepack2 %}
    </a>
{% endif %}
{% endif %}
</td>
<td class="sched">
{% if day.due %}
{% if day.due_link%}
<a href="{{day.due_link}}">
{% endif %}
{{day.due}}
{% if day.due_link%}
</a>
{% endif %}
{% endif %}
{% if day.due2 %}
<br>
{% if day.due_link2%}
<a href="{{day.due_link2}}">
{% endif %}
{{day.due2}}
{% if day.due_link2%}
</a>
{% endif %}
{% endif %}
</td>
</tr>
{% endfor %}
</tbody></table>

_^ NOTE: Per the syllabus, a student's lowest GP score is converted to a max score at the end of the semester, which functions as one free skip.  In-class Guided Practice activities cannot be made up due to the nature of the activities._

## Project Schedule Overview

_See <a href="/project.html#sprint-information">the Sprint Information on the Project Information page</a> for a detailed schedule._

<table class="schedtab"><thead>
<tr>
    <th>Week Of</th>
    <th>Sprint Info</th>
    </tr>
    </thead>
    <tbody>
{% for day in site.data.labschedule %}
{% if day.type == 'holiday' %}
<tr class="holiday">
{% elsif day.type == 'sprint_check' %}
<tr class="quiz">
{% else %}
<tr>
{% endif %}
<td class="text-center sched">{{day.date}}</td>

<td class="sched">
{% if day.link %}
<a href="{{day.link}}">
{% endif %}
{{day.topic}}
{% if day.link %}
</a>
{% endif %}
<br>
{% if day.duedate %}
<span class="sched-sub">
Sprint Due: Sunday {{day.duedate}} at 12:00 PM
</span>
{% endif %}
</td>

</tr>
{% endfor %}
</tbody></table>


## Office Hours Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=n0peik670v06jh9bfb0js1k1k8%40group.calendar.google.com&ctz=America%2FNew_York&mode=WEEK" style="border: 0" width="100%" height="600" frameborder="0" scrolling="no"></iframe>