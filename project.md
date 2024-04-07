---
layout: default
title: Project Information
nav_order: 4
---

# Project Information
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Project Overview

This semester, we are doing something a bit different from previous semesters.  As a class, we are going to focus on one particular type of software system - a "whistleblower" app.  The technical requirements are going to be firmer up front, but your team will still have the ability to customize the theme of the app (e.g., whistleblower to a news organization, whistleblower to the honor committee about an honor violation, etc.) and some of the extended functionality.

You __must__ meet the base requirements listed below.

## Base Requirements

- All projects must incorporate Google user accounts as the primary way that someone logs into the system. You will need to use the Google account API to make this work. There are several libraries that are built for Django to work with Google accounts with tutorials.

- There are four different user types you have to consider:
	- Anonymous users
	- Common users with accounts
	- Site Admins who login to receive what has been submitted (and CANNOT access the Django admin page)
	- Django Admins that only have access to the Django Admin page (and NOT the app)

- The accounts we will use are:
	- Anonymous testing - no user
	- Common user - cs3240.student@gmail.com
	- Site Admin user - cs3240.super@gmail.com
	- Django Admin user - cs3240.django@gmail.com / user: admin / pass: admin

- All projects must incorporate cloud storage through Amazon S3 to handle submissions from whistleblowers.  No submissions should be stored in Heroku as they will be deleted when your dyno is restarted!

- Your system must be able to accept the following file types:
	- .txt / plain text
	- .pdf / Adobe PDF documents
	- .jpg / JPEG Images
- You can have additional file types, but the ones above must be accepted.

- All projects must be built using the prescribed language (Python 3), database system (PostgreSQL), framework (Django 5), build environment (GitHub Actions CI), source control management (GitHub), cloud hosting (Heroku), and cloud storage (Amazon S3). No exceptions to these will be granted.
	- Note: All projects must use the PostgreSQL database engine for production on Heroku and continuous integration (on GitHub Actions). You are allowed to use SQLite for local testing so you do not have to install PostgreSQL on your own machine, but another option is to change your `settings.py` file point to the PostgreSQL DB on Heroku at all times.

- All projects should have a footer on each page that indicates that this system is a class project, the system is not monitored, and no real information should be submitted.  If appropriate, direct the user to an appropriate external resource.

## Core Use Cases

### Anonymous User
{: .no_toc }

- The system shall allow an anonymous user to make a submission with the following at a minimum:
	- Text field to allow free form text submission
	- The ability to upload multiple files at the same time (see allowed file types above)
- Teams can add additional fields/functionality based upon their requirements elicitation.
- NO INFORMATION about the anonymous user should be retained!

### Common User
{: .no_toc }

- The system shall allow a common user to create an account in the system using their Google account.
- If a common user makes a submission (see Anonymous user submission), then the submission information should be recorded in such a way that the common user can view a history of their previous submissions.
- A common user shall be able to delete any previous submission.  No record of the submission should be retained (no files in cloud storage or record in the DB).
- A common user shall be able to see if their submission has been reviewed by a site admin user.

### Site Admin User
{: .no_toc }

- A site admin user shall be created by having their account elevated to site admin status by a Django admin user logging in to the Django admin site and making the change to the account there.  Only a Django admin can grant site admin user privileges.
- A site admin user shall be able to see a list of all submissions made, along with associated files.  Site admin users can view submissions and files within the website interface.
- __Deprecated Requirement:__ ~~A site admin user can mark a submission as having been reviewed, which will be indicated to common users in their list of submissions.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been reviewed.~~
- __Changed Requirement:__ An incoming submission to the system from a user is initially marked as "New."  When a site admin first views the submission, the submission's status should change from "New" to "In Progress."  If the submission came from a user with an account, they can see the changed status of their submission.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been reviewed.
- __New Requirement:__ When a site admin completes their action on the submission, they can set the status to "Resolved."  Also, the system shall allow the admin to submit text notes explaining what the resulting action of the submission was.  If the submission came from a user with an account, they can see the changed status of their submission and can read the explanation text from the site admin.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been resolved.

### Django Admin User
{: .no_toc }

- A Django admin user is created only through the `createsuperuser` Django command.
- A Django admin user should be treated as a common user if they try to login to the app itself.
- No other account type should have access to the Django admin site.
- Django admins have the ability to change a common user into a site admin user by changing a value in the user record through the Django admin site.

## Variations and Themes
{: .no_toc }

- Your team's app can take the requirements above and place the app in whatever domain your team is interested in.
- Extended requirements for your app will come from the requirements elicitation activity you will in the first few weeks of class.


## Team Roles

Each member of your five person team will take on one of these roles.  Each role has different responsibilities, but ALL ROLES require that you be an active contributor to the code of the project.  In other words, if you take on Scrum Master, that doesn't mean you don't have to contribute as much code as someone else.  Please see the [information on Assessment and Grading](/syllabus.html#assessment-and-grading) for more information.

__Scrum Master__ - The Scrum Master could also be called the Team Leader, but it's not really a "leader" position, per se, in that they are not making major decisions about the project itself.  The Scrum Master is responsible for keeping everyone on track, facilitating all team meetings, and monitoring team status / issues.  The course staff will come to the Scrum Master first if there are any team issues or questions, and similarly the Scrum Master needs to know what's going on with the team and can communicate with the staff if someone is falling behind, etc.

- Reasons to be the Scrum Master: You like keeping schedules; you like keeping things organized; you don't mind being the point of contact with the staff.
- Reasons not to be the Scrum Master: You are not the most organized person; you don't think you can stay on top of what the team is working on; you don't like talking to the staff.

_Major Artifact_: [Scrum Master Final Report]({{ site.data.externallinks.scrum_master_report_template }}), due at the end of the semester   

__Requirements Manager__ - The Requirements Manager is responsible for keeping up with the features of the project.  This person will take the lead on the requirements elicitation process (which takes place in the first couple weeks of the project) as their major activity.  Note that the Requirements Manager doesn't do the whole process - they just lead the effort.  Everyone else has to participate as well!  Then throughout the semester they will manage the feature/issue tracker in GitHub, monitoring the state of the project.

- Reasons to be the Requirements Manager: You are interested in learning how requirements are created; you want to find out what your fellow students are excited about with your project; you like updating a spreadsheet; you like knowing "what's coming next" in the project.
- Reasons to not be the Requirements Manager: You have no interest in interacting with other people to find out what they want in a system; your first couple weeks of the semester are super hectic and you don't have the time for the elicitation process.

_Major Artifact_: [Requirements Elicitation Document]({{ site.data.externallinks.requirements_report_template }})  , due within the first few weeks of the semester    

__Testing Manager__ - The Testing Manager is responsible for ensuring that the system is thoroughly tested, for developing the overall testing plan/philosophy of the team, and spearheading the beta testing effort at the end of the semester.  The Testing Manager is responsible for executing beta testing at the end of the semester and creating the Beta Testing Document.  The Testing Manager is also responsible for overseeing that philosophy throughout the semester, ensuring unit tests are being written.  Note that the Testing Manager does not write every test case in the system - they just keep up with what everyone else is doing and lend support as needed.

- Reasons to be the Testing Manager: You want to learn more about testing procedures; you love seeing that unit test result bar turn green; you took HCI or something similar and are interested in setting up user testing.
- Reasons not to be the Testing Manager: You don't see the value in writing tests; you don't want to work with your fellow students in doing in-person testing.

_Major Artifact_: [Beta Testing Report]({{ site.data.externallinks.beta_testing_report_template }}), due near the end of the semester    

__DevOps Manager__ - The DevOps Manager is the support tech for the team in a sense.  They are responsible for the management and support of all the systems we are using in the class, namely GitHub, GitHub Actions, and Heroku.  They should be a person that is relatively comfortable tinkering with computers and settings.  The DevOps Manager does not have to have all the answers, but would be the contact person for going to the staff to get help on any particular issues.

- Reasons to be the DevOps Manager: You are familiar with the tools mentioned already, or you are really interested in learning more about them; you like to tinker with settings to get things working "just right"; you have the patience to help those on your team who might need assistance getting their environments working.
- Reasons not to be the DevOps Manager: You do not feel comfortable helping others with technical issues; you are very unfamiliar with the tools above and would rather just have a "turnkey" solution for doing your work this semester.

_Major Artifact_: [DevOps Report]({{ site.data.externallinks.devops_report_template }}), due near the end of the semester  

__Software Architect__ - Midway through the project, a requirements change will be introduced to the base requirements listed above.  The job of the Software Architect is to determine how to implement the change, document the steps that need to be taken, and then help the team implement the change.  The Software Architect is _not_ the primary coder for the project and should not be treated as such.  

- Reasons to be the Software Architect: You enjoy solving a puzzle using critical thinking and you are interested in how software is put together.
- Reasons not to be the Software Architect: You hate troubleshooting code.

_Major Artifact_: [Requirments Change Analysis]({{ site.data.externallinks.sa_report_template }}), due after the requirements change is introduced  

__Sixth Team Member__ - If your team has 6 members, the member without a role listed above should come to office hours with the professor to discuss options.  The role will be determined based on interest and needs of the team.

## Artifact Document Templates

### Team Documents
{: .no_toc }
[Sprint Report]({{ site.data.externallinks.sprint_report }})    
[Final Submission Pledge]({{ site.data.externallinks.final_submission_pledge }})

### Scrum Master
{: .no_toc }
[Scrum Master Final Report]({{ site.data.externallinks.scrum_master_report_template }})

### Requirements Manager
{: .no_toc }
[Requirements Elicitation Document]({{ site.data.externallinks.requirements_report_template }})      

### Testing Manager
{: .no_toc }
[Beta Testing Report]({{ site.data.externallinks.beta_testing_report_template }})

### DevOps Manager
{: .no_toc }
[DevOps Report]({{ site.data.externallinks.devops_report_template }})

### Software Architect
{: .no_toc }
[Requirments Change Analysis]({{ site.data.externallinks.sa_report_template }})

## Sprint Information

For each sprint check, your team must meet the minimum requirements shown below for each sprint to earn full XP.  Faculty will not override a TA's decision except in extreme circumstances.  

Each sprint is graded out of 25 XP.  In general, the following grading standard applies:

- 25 XP: Excellent progress toward completing the project on time and meeting all requirements.
- 20 XP: Good progress toward completing the project, but at least one requirement looks a bit uncertain.
- 15 XP: Fair progress toward completing the project, but team will need to step up to finish successfully.
- 10 XP: Poor progress toward completing the project and the team definitely needs to refocus.  Some measurable work was accomplished, however.
- 5 XP: Little progress was made toward completing the project during this sprint.
- 0 XP: Project is in danger.

### Sprint 1: {{site.data.semesterinfo.sprint_1.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_1.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_1.sprint_check}}

__Goal:__ Have your initial meeting as a team and determine who will be doing what on the team.  This meeting can be any time between when your team is formed and your sprint check meeting with your TA on the first Sunday or Monday of the sprint.  The Scrum Master of each team MUST complete this form with the team as a part of the Sprint: [Team Declaration Form]({{ site.data.externallinks.team_declaration_form }}).  Also, Scrum Masters should initialize the team GitHub repo through [GitHub Classroom]({{ site.data.externallinks.github_classroom_project }}).  Please use your assigned team number for the identifier when prompted (e.g., A-03).  Other team members can then go to that link and accept the assignment, selecting the proper team.

__Requirements:__  Complete the Team Declaration form above ASAP.  Initialize your GitHub repo and have all team members join.

__Team Evals:__ No Team Evals this week.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  (No, you won't have much to report this week, but think about what's coming up and discuss that.)

### Sprint 2: {{site.data.semesterinfo.sprint_2.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_2.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_2.sprint_check}}

__Goal:__ Spend most of this sprint working as a team to elicit the full requirements for your system.  Note that while the final Requirements Document is the responsibility of the Requirements Manager, ALL TEAM MEMBERS are expected to contribute to gathering and refining the final set of requirements.  Once you have a good set of user stories / issues / tasks for your team to work on, add these as Issues to your GitHub Issues page on your team's repository.

__Requirements:__ The team must have a "reasonable" set of user stories / issues in GitHub Issues.  We do not expect you to have your final set of features at this point.  However, you need to be able to show the TA that you have started gathering requirements data and that you have converted at least some of this information into GitHub Issues.  The Requirements Manager will receive a separate score for the requirements document, which is due a week later.

- [Example Requirements Document from Spring 2020](https://docs.google.com/document/d/1l39MWsVEX8LWcQ16Wo5-PXyaKhfm_O6j-1Uj6wj8RUU/edit?usp=sharing)
- ["Excellent" Example from Fall 2020](https://docs.google.com/document/d/1aqeWWhA1QztrM_6iAI1PF3FjP8VTvOqCXhe5w9D9GaU/edit?usp=sharing)
- ["Great" Example from Fall 2020](https://docs.google.com/document/d/12a8MTkqiUZbnDIs-xRfmCQUb8ozs3jHamdcwp6fuqSc/edit?usp=sharing)
- ["Good" Example from Fall 2020](https://docs.google.com/document/d/1RxUBAEFjk0HpQ1aFOOX830nenFBX_Idao3vRVBYop1A/edit?usp=sharing)

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }})

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  Your GitHub Issues page should be populated with your team's project requirements.  (NOTE: If you would like to use GitHub Projects instead of Issues, you may do so.)  The requirements manager should submit the requirements document to the appropriate assignment by the separate due date listed.  No other team members should submit the requirements document.

### Sprint 3: {{site.data.semesterinfo.sprint_3.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_3.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_3.sprint_check}}

__Goal:__ All projects must have a user account feature for students to login with.  To accomplish this, you are to integrate Google login to your app.

__Requirements:__ A user with a Google Account can login to the system and the system shows in some way that that user has indeed logged in.  You should not lock your app to just @virginia.edu accounts.  You must show that both a regular user account _and_ a site admin account can login and that they get different screens.  Note the requirements for the different types of users above.  Print the user's name and account name to the screen to show that it works.  If you want to start working on more requirements, you absolutely can do so.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 4: {{site.data.semesterinfo.sprint_4.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_4.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_4.sprint_check}}

__Goal:__ All projects must allow a user to upload files to Amazon S3.

__Requirements:__ A major component of your system is to allow users to upload files to a permanent storage location (i.e. not directly to your Heroku installation).  Using Amazon S3, implement the necessary features to allow users (anonymous and logged in) to upload the three file types listed in the requirements above and show that the files can be viewed by a site admin through the website itself (not by just going directly to S3.)  GitHub Actions CI MUST be operational with at least multiple test cases in order to earn full XP.  As you are just getting started with testing, this is more showing us that you have the process setup and that you have some passing tests.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 5: {{site.data.semesterinfo.sprint_5.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_5.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_5.sprint_check}}

__Goal:__ The Software Architect takes the lead in guiding the team through the requirements change. 

__Requirements:__ At the beginning of Sprint 5, the staff will introduce a requirements change to the project.  The Software Architect is responsible for leading the team through this change and documenting the needed architectural changes to handle the update.  

The requirements change can be seen above in the Site Admin section of the Base Requirements.  They are also repeated below:

- __Deprecated Requirement:__ ~~A site admin user can mark a submission as having been reviewed, which will be indicated to common users in their list of submissions.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been reviewed.~~
- __Changed Requirement:__ An incoming submission to the system from a user is initially marked as "New."  When a site admin first views the submission, the submission's status should change from "New" to "In Progress."  If the submission came from a user with an account, they can see the changed status of their submission.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been reviewed.
- __New Requirement:__ When a site admin completes their action on the submission, they can set the status to "Resolved."  Also, the system shall allow the admin to submit text notes explaining what the resulting action of the submission was.  If the submission came from a user with an account, they can see the changed status of their submission and can read the explanation text from the site admin.  Anonymous users receive no notifications, but the site admin user can still see that the submission has been resolved.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 6: {{site.data.semesterinfo.sprint_6.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_6.duration}}     
__Sprint Due:__ {{site.data.semesterinfo.sprint_6.sprint_check}}

__Goal:__ After Sprint 6 is complete, you are going to have other students test your system.  So you need a working system with most all of your functionality ready to go.  The app may not be fully polished and still needs a bit of work, but it needs to be usable from beginning to end.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__Requirments and Full Beta Version:__ In the opinion of the TA, you have an app that is ready for other students to test out (e.g. it doesn't crash, it looks reasonably good, it has most features, etc.).  You will earn 25 XP for the sprint check plus 100 XP as the first half of your overall project score of 250 XP (basically, if you have a working app at this point, we know your final project grade will be at least 100/250 XP, so we can give you those points now).

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Beta Testing

__Sprint Duration:__  {{site.data.semesterinfo.beta_testing.duration}}     
__Sprint Due:__ {{site.data.semesterinfo.beta_testing.sprint_check}}

__Goal:__ You now have a "working" version of your project that you can have others use.  Follow the instructions in the Beta Testing Document to have others work through a script of testing your software, similar to what we did with the Guided Practice.  You can ask anyone to test your system, even those currently in CS 3240.  It would be nice to ask at least some folks that you included in your requirements elicitation so they can see what all you have built!  Refer to the lectures where this was discussed for more information.  Once you have done your testing, keep polishing your system for final submission!

### Final Version

__Sprint Duration:__  {{site.data.semesterinfo.final_version.duration}}     
__Sprint Due:__ {{site.data.semesterinfo.project_due_date}}

__Goal:__ It's the final week to polish up your app and make changes based on the Beta Testing feedback!  Good luck!

## Final Grading Information

The final project is worth a total of 250 XP.  (100 XP will be awarded after Sprint 6 for your Beta version and the remaining 150 XP will be awarded by the professors after final demos.)  Like the other assessments in this course, grading is overall wholistic - that is, there is no specific point-for-point breakdown for the rubric.  One reason for this is that this is simply not how software is delivered in real-life.  There are basically only four outcomes:

- You meet the expectations of the customer within reason and both parties are satisfied with the outcome;
- You exceed the expectations of the customer, potentially generating more good will, a good reference, or more future business;
- You do not quite meet the expectations of the customer, leaving some room for improvement;
- You ship a system that simply does not work to the expectations of the customer.

We will grade your projects in a similar vein, with some flexibility for minor adjustments.

Thus, the grading levels will be:

- Above and Beyond - Min XP: 250 / Max XP: 255
- Complete - Min XP: 200 / Max XP: 250
- Lacking - Min XP: 150 / Max XP: 200
- Insufficient - Min XP: 0 / Max XP: 150

Aspects that will determine the exact grade within a range include but are not limited to:

- UI design
- Overall flow of application
- Special features
- Obvious bugs that should have been corrected
- Polish

__Final Team Evals:__ All team members will complete a final, overall team evaluation at the end of the course.  [Final Student Team Sprint Evaluations]({{ site.data.externallinks.final_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__The final version of the project must be in GitHub and hosted on Heroku no later than {{ site.data.semesterinfo.project_due_date }}!__