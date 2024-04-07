---
layout: default
title: Syllabus
nav_order: 2
---

# Course Syllabus
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Basic Info
{: .no_toc }
Spring 2024 Semester   
https://s24.cs3240.org   

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

## Communication and Logistics

### Textbook / Online Coursepack
{: .no_toc }

There is no official textbook for the course that you need to purchase.  We have our own online coursepack using the video content we created during COVID, which is available at [{{ site.data.externallinks.coursepack }}]({{ site.data.externallinks.coursepack }}).
### Discord
{: .no_toc }

We will be using Discord for the following:

* Online office hours (TAs)
* Online team meetings and discussions
* General project / course discussion
* Off-topic channels for general discussion

We will not be using Discord for:

* Long-form project questions / help (use Piazza or go to office hours)
* Regrades (use Gradescope first, then office hours only if not resolved)
* Direct messaging the staff about code questions, etc. (use Piazza)
* Direct messaging the faculty about sensitive / grading issues (use private messages in Piazza or email)

More information about joining our Discord server will be available in Canvas at the start of the semester.

### Piazza
{: .no_toc }

Piazza @ [{{ site.data.externallinks.piazza }}]({{ site.data.externallinks.piazza }})    

We will be using Piazza for the following:

* Long-form questions about the class, code, or project (please post all code privately!)
* Private messages for faculty or the entire staff
* A searchable repository of common questions in the course about the project, assignments, etc.

We will not be using Piazza for:

* Regrades (use Gradescope first, then office hours only if not resolved)
* Meme posting (use Discord :-) )

### Email
{: .no_toc }

We will be using email for the following:

* Personal issues that can and should only be handled by a professor
* Team issues that need to be escalated beyond the TA

We will not be using email for:

* Regrades (use Gradescope first, then office hours only if not resolved)
* Tech help (use Piazza)
* Project questions (use Piazza)
* Guided Practice questions (use Piazza)

You should, in general, email the professor for the section that you are enrolled in.  _PLEASE_ make sure to put "CS 3240" in the subject line somewhere so we can keep track of your request!  And please be patient with us in responding.  We all receive A LOT of email and it's easy to get behind.  If there is a time-critical nature to your note, please let us know that as well.

### Where or who do I ask about...?
{: .no_toc }

* Team meetings -> Discord
* Online office hours (TA) -> Discord
* Technical questions (python, django, heroku, etc.) -> Piazza or TA office hours
* Project requriements -> Piazza or office hours
* Regrades -> Gradescope (office hours only if issues with Gradescope)
* Personal issues -> Email your professor
* Team issues -> Email your TA and/or your professor

For the context of the project, you should consider the professor "upper management" and the TAs "senior developers / managers."  Thus, high-level, requirements-based, or course-management sort of questions should go to the professor, while all technical and initial grading questions should to go the TAs.  (Honestly, you're probably going to get a faster, better answer to a Django question if you go to the TAs... sure, the professor can answer it... eventually... after a lot of Googling... but you could also ask a TA who did the project last semester or has been a TA for several semesters...)

## Course Description
Analyzes modern software engineering practice for multi-person projects; methods for requirements specification, design, implementation, verification, and maintenance of large software systems; advanced software development techniques and large project management approaches; project planning, scheduling, resource management, accounting, configuration control, and documentation. 

### Course Objectives
{: .no_toc }   
Upon completion of this course students will:

* Develop an understanding of how to specify, design, and implement a complex software entity that involves many aspects of modern software systems. 
* Master a number of modern tools and a number of difficult technical fields. 
* Acquire experience of working on a large software system as a member of a team working on system development and as a member of a team that has to interact with other teams and customer representatives.

### Course Topics
{: .no_toc }    
The topics to be covered in the course include:  

* Software quality, including testing and inspections
* Project management, scheduling, planning, with an emphasis on the Scrum agile method
* Requirements elicitation, analysis and specification
* Architecture and design principles
* Security in the development of software applications
* Programming and team-based development practices
* Professional ethics

### Course Requirements
{: .no_toc }
You should meet the following requirements to take this class:

1. __Prerequisite: CS 2150 --OR-- CS 3140 with a grade of C- or higher.__  Students that do not meet this prerequisite may be dropped at any point from the class.  It is the student's responsibility to check this prerequisite and/or speak with the instructor ASAP.
2. Willing and able to attend in-person lectures.
3. Be a meaningful contributor to your team project, which includes your team role responsibilities AND writing code that will be incorporated into the final version of the product.
4. You will be expected to learn programming languages and platforms on your own in this class! If you don’t feel comfortable with this, please talk to the staff as soon as possible!

## Assessment and Grading
We will utilize a positive-reinforcement grading policy in this course. As the purpose of this class is for you to gain experience as a software developer working in a team on a larger-scale project, your grade in this course will be based on experience points (XP). Every student begins the course with 0 XP.  As you complete assessments, work on the project, and complete Guided Practice activities, you will earn XP.  Some assessments will have a way to retake or resubmit to earn some of the XP that was not earned on the first attempt.  Please see individual assessments for more information regarding how this mechanic works.

| Assessment	| Who	| Instances	| Max XP 	| Max XP Avail |
|:--------------|:-----|:---|:-----|:-----|
|Guided Practice |	Small Groups or Individual |	10 |	5 |	50 |
|Team Role Document |	Individual |	1 |	100 |	100 |
|Team & Staff Evaluation |	Individual |	1 |	100 |	100 |
|Quizzes |	Individual |	3 |	100 |	300 |
|Project Sprints |	Team |	6 |	25 |	150 |
|Project (Beta Version) | Team | 1 | 100 | 100 |
|Project (Final Version) |	Team |	1 |	150 |	150 |
|Django Practice |	Individual |	1 |	50 |	50 |
| __Total Course XP__ | | | | 1000 |

| Letter Grade | XP Required |
| ------------ | ----------- |
| A+           | 1000        |
| A            | 950         |
| A-           | 900         |
| B+           | 875         |
| B            | 850         |
| B-           | 825         |
| C+           | 775         |
| C            | 750         |
| C-           | 700         |
| D+           | 675         |
| D            | 650         |
| D-           | 625         |

### Assessment Notes
{: .no_toc }

* Your one lowest GP is converted to 5 XP at the end of the semester.  This should primarily be used in case you are ill or must miss class for some other reason. 
* Due to the nature of most in-class GPs, these cannot be made up if they are missed.
* Each of the five team roles has a different document to submit that demonstrates an aspect of the position.
* Your evaluation score is based upon several intermediate evals from teammates throughout the semester, a final evaluation from teammates, and the opinion of the staff.
* There are 3 total quizzes, which will be taken in-person during lecture. Students can earn back up to 100 XP from missed quiz questions on the final exam.
* There are 6 sprints during the project.  At each sprint check, the TAs will determine if your team has met the requirements for the project up to that point.  
* We expect __all students__ to __fully participate__ in the coding of the project.  This includes:
  - Working successfully with other team members
  - Attending team meetings (both with and without the TA)
  - Collaborating on code with team members
  - Committing working, meaningful code to the project on the main branch that makes it to the final version of the system (e.g. coding a feature of the system, not just fixing deployment issues or adding test cases)
* Students who do not fully participate in the project per the information above will have XP _removed_ from various team-related scores, including the sprint scores, final team project score, and team evaluation score.  We do this because if the student did not fully participate, then that XP was not properly assigned because they gained no experience through the work.  Removing XP will be represented as a negative team evaluation score in our system so as to make the penalty clear to the staff and student.

### Final Exam and Project Demos
{: .no_toc }

__Final Exam:__ The final exam in this course is an opportunity to show mastery of material that was previously missed on earlier quizzes.  If a student has earned the maximum number of points on the three quizzes, they have a set of scores they are comfortable with, or if they already have an A in the course, the student does not (and should not) take the final exam.  If a student wishes to take the final exam, they can earn back up to 100 XP total toward the available 300 XP from quizzes.  We will create a custom final exam for each student based upon only the questions the student missed on the previous three quizzes.  While it is possible to lose points on the final exam, this is a relatively rare occurance, usually stemming from wild guessing on questions.  Students can come to either exam session, regardless of enrolled section.

__Project Demos:__ Student teams will demo their final project to a professor near the end of the semester.  All students are expected to attend the demo for their team.  Demos should only last around 20 minutes.  Students do not need to prepare anything for the demo (e.g. no slides, no presentation, etc.).  The team will walk the professor through the app and will answer various questions about its design and implementation.

## Class Management

### Project Groups
{: .no_toc }
You are expected to work as a member of your group in this course and cooperate with your colleagues. Cooperation means attending group meetings, completing your assignments properly and on time, letting your group know if you will be out of contact, responding to e-mail from your group, and so on. If there is a lack of cooperation by any group member, it must be brought to the attention of the instructor as soon as it happens. If the lack of cooperation is serious, the offending group member’s semester grade will be lowered (see information above under Assessment).  _Note that this can result in a student automatically failing the course!_

### Attendance
{: .no_toc }
* No attendance will be taken during the lectures sessions on Tuesdays and Thursdays.  
* We do not plan to record lectures this semester to better encourage attendance and participation.  Recordings from previous semesters will be available for students who have to miss class.
* Students should only attend the lecture section they have registered for due to room size restrictions.  
* Guided Practice activities will take place during announced class sessions.  Some of these will be in-class only, while some can be done outside of class time.  Also note that some Guided Practice activities _must_ be done in teams and cannot be done solo or even in pairs.  Pay attention to the instructions.

### Late Policy
{: .no_toc }
* Late work grace periods are built into Gradescope where appropriate.  Further exceptions require professor approval.  
* In general, late work will not be accepted - either for individual or group work.

### This Syllabus
{: .no_toc }
This syllabus is to be considered a reference document that can and will be adjusted through the course of the semester to address changing needs. This syllabus can be changed at any time without notification. It is up to the student to monitor this page for any changes. Final authority on any decision in this course rests with the professor, not with this document.

### Professionalism
{: .no_toc }
In this course, there will be a focus on working well together and learning about the development process. A large portion of that process involves interpersonal skills and conflict management. Students and staff are all expected to treat each other with respect.  This includes, but certainly is not limited to:

* Proper use of class platforms (Discord, Piazza, YouTube comments, etc.)
* Respectful behavior in class (including extraneous internet browsing, social media, phone usage, etc.)
* Respectful language or actions to course staff or other students
* Promptness for all deadlines and class meetings
* Quality work
* Working well with your partners
* Following the honor code and other collaboration policies
* Following any University health and safety regulations

Students can and will be penalized for unprofessional behavior.  This will be represented as a negative XP score on the Team/Staff Evaluation.

## Academic Integrity
_Summary_:

* Know the honor code
* Work with your team, but not any other team
* Using code from other students (from any semester) is an honor violation
* Using publically-available example code and libraries is fine, but you must cite your resources
* More information on what is allowed will be included with each assignment if necessary
* It never hurts to ask the staff what is allowed or not allowed!

The School of Engineering and Applied Science relies upon and cherishes its community of trust. We firmly endorse, uphold, and embrace the University’s Honor principle that students will not lie, cheat, or steal, nor shall they tolerate those who do. We recognize that even one honor infraction can destroy an exemplary reputation that has taken years to build. Acting in a manner consistent with the principles of honor will benefit every member of the community both while enrolled in the Engineering School and in the future. 

Students are expected to be familiar with the university honor code, including the section on academic fraud [http://honor.virginia.edu/academic-fraud](http://honor.virginia.edu/academic-fraud). Assessments will describe allowed collaborations, and deviations from these will be considered Honor violations. If you have questions on what is allowable, ask! Unless otherwise noted, all assessments will be considered pledged that you have neither given nor received help. (Among other things, this means that you are not allowed to describe problems on an exam, assignment, or project to a student who has not taken it yet. You are not allowed to show exam papers to another student or view another student’s exam papers while working on an exam.) Sending, receiving, or otherwise copying or describing the contents of electronic files that are part of course assignments are not allowed collaborations (except for those explicitly allowed in assignment instructions). 

Assignments or exams where honor infractions or prohibited collaborations occur will receive a zero grade for that entire assignment or exam. Such infractions will also be submitted to the Honor Committee if that is appropriate. Students who have had prohibited collaborations may not be allowed to work with partners on remaining homeworks. 

For CS 3240, using code developed by previous students in the course or code written for your use by someone outside the course is not allowed and will likely be an honor violation. This does not apply to the use of publicly available frameworks and libraries, unless indicated in the assessment instructions.

In general, we expect that you will be using code, examples, and ideas from many different websites and resources for your projects.  This is allowed within reason.  Wholesale copying of an entire project or any major feature from any source (the web, another student, etc.) is definitely not allowed.  Using code snippts that you find to round out a feature is allowed.  If you ever have a question about what is or is not appropriate, ask first!

In ALL cases, you need to cite all sources at the top of the file where the code or algorithm was used AND you should note all sources in your documentation.  Failure to properly attribute your sources will result in a 50% penalty for the project at a minimum.

## How to Cite Code
{: .no_toc }
Use the following general format as an example for citing code you use. You may not have all of these fields available, but this should give you a good idea of things to look for.  Use the appropriate commenting format for the programming language of your source code.  Does yours have to look *exactly* like this?  No, it just has to have enough to give the proper credit and so we can find the resource if needed.

```
/***************************************************************************************
*  REFERENCES
*  Title: <title of program/source code>
*  Author: <author(s) names>
*  Date: <date>
*  Code version: <code version>
*  URL: <where it's located>
*  Software License: <license software is released under>
*
*  Title: ....
*
***************************************************************************************/
```

## Policy on Use of Generative AI
{: .no_toc }
In general, we will treat the use of generative AI the same as we would a student asking for help on StackOverflow or finding other sources of code.  For coding questions (i.e. "How do I make Google login work with Django?"), students are welcome to use generative AI.  This includes tools such as ChatGPT, GitHub Copilot, and other code completion systems.  (NOTE: We actually asked ChatGPT the question above and it came back with a pretty good answer!  WeI suggest trying it!)  

For artifact documents and other writing prompts, generative AI is discouraged and honestly won't be of too much help regardless.  While these tools can give you some impressive boilerplate text that would work for a generic presentation, it's not going to have the specific details of what your team had to do to make your project a success, and that's what we are specifically assessing.  So, if you lean too heavily on generative AI, your submission isn't going to earn much XP (if any) because we really don't want to read a bunch of generic "why is devops good" sort of text.  We care a lot more about how your team was impacted.

## Miscellaneous Policies

### Inclement Weather Policy
{: .no_toc }
If there is the possibility of inclement weather that could affect class, it is your responsibility to stay informed.  Information about how to sign up for email and/or text alerts from UVA Emergency Management, along with the current University status, can be found at [https://uvaemergency.virginia.edu/](https://uvaemergency.virginia.edu/).

### SDAC and Other Special Circumstances
{: .no_toc }
It is our goal to create a learning experience that is as accessible as possible. If you anticipate any issues related to the format, materials, or requirements of this course, please make an appointment to with your instructor outside of class so we can explore potential options. Students with disabilities may also wish to work with the Student Disability Access Center (SDAC) to discuss a range of options to removing barriers in this course, including official accommodations. We are fortunate to have an SDAC advisor, Courtney MacMasters, physically located in Engineering. You may email her at [cmacmasters@virginia.edu](mailto:cmacmasters@virginia.edu) to schedule an appointment. For general questions please visit the SDAC website: [sdac.studenthealth.virginia.edu](http://sdac.studenthealth.virginia.edu). 

If you have already been approved for accommodations through SDAC, please send your instructor your accommodation letter as soon as possible. We happily and discretely provide the recommended accommodations for those students identified by the SDAC. For quizzes and other individual assessments, please remind us one week before an exam so we can make accommodations.  For team related assessments, we cannot grant significant accommodations to deadlines for an entire team due to accommodations of individuals on the team. However, we are more than happy to discuss with you the best way to integrate with your team with your accommodations in consideration. Please make an appointment with your instructor outside of office hours to have this discussion.

If you have other special circumstances (athletics, other university-related activities, etc.), please contact the instructor as soon as you know these may affect you in class.

### Health Accommodations
{: .no_toc }
It is in the best interest of everyone in our community to keep the spread of infectious disease to a minimum.  If you are ill, please do not come to class.  Lectures from previous semesters will be made available along with the course materials on the course pack and you can follow along there.  Quiz accommodations can be made on a case-by-case basis.  Due to their team-based nature, certain Guided Practices cannot be made up, but we build in a free drop into the Guided Practice grading to handle these cases.  If a student must miss an excessive number of Guided Practices, they should meet with the instructor to discuss options.

### Religious Accommodations
{: .no_toc }
It is the University's long-standing policy and practice to reasonably accommodate students so that they do not experience an adverse academic consequence when sincerely held religious beliefs or observances conflict with academic requirements.

Students who wish to request academic accommodation for a religious observance should submit their request to their instructor by email as far in advance as possible. Students who have questions or concerns about academic accommodations for religious observance or religious beliefs may contact the University’s Office for Equal Opportunity and Civil Rights (EOCR) at [UVAEOCR@virginia.edu](mailto:UVAEOCR@virginia.edu) or 434-924-3200.

Accommodations do not relieve you of the responsibility for completion of any part of the coursework - including the team project - missed as the result of a religious observance.

### Support for Career Development
{: .no_toc }
Engaging in your career development is an important part of your student experience. For example, presenting at a research conference, attending an interview for a job or internship, or participating in an extern/shadowing experience are not only necessary steps on your path but are also invaluable lessons in and of themselves. We wish to encourage and support you in activities related to your career development. To that end, please notify your instructor by email as far in advance as possible to arrange for appropriate accommodations.

### Student Support Team
{: .no_toc }
You have many resources available to you when you experience academic or personal stresses. In addition to your professor, the School of Engineering and Applied Science has staff members located in Thornton Hall who you can contact to help manage academic or personal challenges. Please do not wait until the end of the semester to ask for help! 

__NOTE:__ These resources are available for BACS majors as well!  You are still a part of our department!

### Learning
{: .no_toc }
* [Lisa Lampe](https://engineering.virginia.edu/current-students/current-undergraduate-students/student-support/academic-coaching), Director of Undergraduate Education
* [Georgina Nembhard](https://engineering.virginia.edu/current-students/current-undergraduate-students/student-support/academic-coaching), Director of Undergraduate Success 
* [Courtney MacMasters](mailto:cmacmasters@virginia.edu), Accessibility Specialist
* [Free tutoring](https://engineering.virginia.edu/current-students/current-undergraduate-students/student-support/tutoring) is available for most classes

### Health and Wellbeing
{: .no_toc }
* [Kelly Garrett - Assistant Dean of Students](https://engineering.virginia.edu/about/offices/office-graduate-programs/student-support-services#accordion716460), Student Safety and Support  
* Elizabeth Ramirez-Weaver, CAPS counselor
* Katie Fowler, CAPS counselor

You may schedule time with the CAPS counselors through [Student Health](https://www.studenthealth.virginia.edu/getting-started-caps). When scheduling, be sure to specify that you are an Engineering student or College student. You are also urged to use [TimelyCare](https://www.studenthealth.virginia.edu/timelycare) for either scheduled or on-demand 24/7 mental health care. 

### Community and Identity
{: .no_toc }
The [Center for Diversity in Engineering](https://engineering.virginia.edu/about/diversity-and-engagement/center-diversity-engineering) (CDE) is a student space dedicated to advocating for underrepresented groups in STEM. It exists to connect students with the academic, financial, health, and community resources they need to thrive both at UVA and in the world.  The CDE includes an open study area, event space, and staff members on site. Through this space, we affirm and empower equitable participation toward intercultural fluency and provide the resources necessary for students to be successful during their academic journey and future careers.


### Statement on Violence
{: .no_toc }
The University of Virginia is dedicated to providing a safe and equitable learning environment for all students. If you or someone you know has been affected by power-based personal violence, more information can be found on the [UVA Sexual Violence website](http://www.virginia.edu/sexualviolence) that describes reporting options and resources available.  

The same resources and options for individuals who experience sexual misconduct are available for discrimination, harassment, and retaliation.  [UVA prohibits discrimination and harassment](https://uvapolicy.virginia.edu/policy/HRM-009) based on age, color, disability, family medical or genetic information, gender identity or expression, marital status, military status, national or ethnic origin, political affiliation, pregnancy (including childbirth and related conditions), race, religion, sex, sexual orientation, veteran status. [UVA policy](https://uvapolicy.virginia.edu/policy/HRM-010) also prohibits retaliation for reporting such behavior. 

If you witness or are aware of someone who has experienced prohibited conduct, you are encouraged to submit a report to [Just Report It](https://justreportit.virginia.edu/) (justreportit.virginia.edu) or [contact EOCR](mailto:UVAEOCR@virginia.edu), the office of Equal Opportunity and Civil Rights.

If you would prefer to disclose such conduct to a confidential resource where what you share is not reported to the University, you can turn to [Counseling & Psychological Services (“CAPS”)](https://www.studenthealth.virginia.edu/caps) and [Women’s Center Counseling Staff and Confidential Advocates](https://womenscenter.virginia.edu/confidential-advocates) (for students of all genders).  

As your professor and as a person, know that I care about you and your well-being and stand ready to provide support and resources as I can. As a faculty member, I am a responsible employee, which means that I am required by University policy and by federal law to report certain kinds of conduct that you report to me to the University's Title IX Coordinator. The Title IX Coordinator's job is to ensure that the reporting student receives the resources and support that they need, while also determining whether further action is necessary to ensure survivor safety and the safety of the University community. 


## Frequently Asked Questions

__Q: Can we pick our own teams?__   
A: No.  There are solid, pedagogical reasons to have randomly assigned teams.  Also, the purpose of this class is to learn about how to work together with others on a project.  If you are already friends, then that negates that part of the learning objectives.

