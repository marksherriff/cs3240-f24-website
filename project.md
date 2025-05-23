---
layout: default
title: Project Information
nav_order: 4
---

# Team Project Information
{: .no_toc }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Team Project Overview

This semester, we are going to be fully focused on projects... literally!  You're going to be building a project management application!  We are going to give you some specific technical requirements that you will have to meet to ensure that all teams are building something that is roughly the same "difficulty."  However, you will have the ability to customize the theming of the app.  The projects could be working with other students on homework assignments, student group event planning, or perhaps related to a hobby you are intersted in.  You will also extend the functionality to better meet the needs of your particular set of users.

From here on, we will refer to your team projects as "Project Management Apps" (PMAs) and "projects" will refer to the "primary object" that you will be building around in your apps.

## Base Requirements

All PMAs __must__ meet the base requirements listed below.

1. All projects must incorporate Google user accounts as the primary way that someone logs into the system. You will need to use the Google account API to make this work. There are several libraries that are built for Django to work with Google accounts with tutorials.
1. There are four different user types you have to consider:
	- Anonymous users: users that will go to your PMA that do not have accounts and want to look around with limited access
	- Common users: users that have accounts in the PMA and will have a login (through Google), a profile, and can create and join projects (within the limits of the app)
	- PMA administrators: users that have accounts in the PMA and will have a login (through Google) and who can see and delete all projects and files, but cannot create or join projects
	- Django administrators: users who have access to the Django Admin page through the Django login system (do not have to use Google login) and have no access to the app
1. We will refer to PMA users that have accounts (common users and PMA administrators) as "regular users."  Regular users DO NOT include anonymous users (because they cannot login to the system) or Django administrators (because they ONLY have access to the Django admin page, and not the PMA itself).
1. Regular users must only login through Google login and NOT through the Django login system.  PMAs SHOULD NOT provide a Django login page for regular users.  
1. PMAs must provide a separate login page for Django admin users.  This page is typically auto-generated by Django and is at the `/admin` URL.  Teams are welcome to customize this page if they want.  Regular users should not be able to login to the Django admin site.
1. All projects in a PMA must have the ability to have [0 to many] files associated with them.  Examples may include: PDFs of homework assignments that teams are working on for a teamwork PMA, images of box art of DVDs for a collection management PMA, etc.
1. All PMAs must incorporate cloud storage through Amazon S3 to handle file uploads.  No uploads should be stored in Heroku as they will be deleted when your dyno is restarted!  Also no files should be stored in the PostgreSQL database as this is generally bad practice.  Application data, such as users, projects, etc. will be stored in the PostgreSQL database.
1. PMAs must be able to accept the following file types:
	- .txt / plain text
	- .pdf / Adobe PDF documents
	- .jpg / JPEG Images
1. You can have additional file types, but the ones above must be accepted.

1. All projects must be built using the prescribed language (Python 3), database system (PostgreSQL), framework (Django 5), build environment (GitHub Actions CI), source control management (GitHub), cloud hosting (Heroku), and cloud storage (Amazon S3). No exceptions to these will be granted.
	- Note: All projects must use the PostgreSQL database engine for production on Heroku and continuous integration (on GitHub Actions). You are allowed to use SQLite for local testing so you do not have to install PostgreSQL on your own machine, but another option is to change your `settings.py` file point to the PostgreSQL DB on Heroku at all times.

1. All PMAs should have a footer on each page that indicates that this system is a class project, the system is not monitored, and no real information should be submitted.  If appropriate, direct the user to an appropriate external resource.

## Core Use Cases and Features

### Projects
{: .no_toc }

1. Projects are the "primary objects" in the PMA.  They must contain, at a minimum:
	- Title
	- Owner (which will be a Common User)
	- A list of Members (which will be a set of [0 to many] Common Users)
	- Description
	- [0 to many] files uploaded to Amazon S3 _(Clarification: This means multiple files over time.  It does not have to support multiple files in a single submission.)_
	- A set of messages posted for the project, implemented as part of the PMA (i.e. not using an external app) 
1. All members of a project can see all messages and files associated with the project.
1. _New Requirement:_ Each file should also have certain metadata associated with it that users can add when they upload the file.  The metadata does not have to be able to be edited after submission, but the users would appreciate it.  Metadata for files should include at a minimum:
	- File title (not the .pdf file name)
	- Timestamp of submission
	- A text description of the contents of the file (Example: "This file contains the meeting minutes for Oct. 21, 2024.")
	- A list of keywords allowing the file to be quickly identified (Example: Minutes, Event Planning, Map, etc.)
1. Things that can be included in a project, but are not required, include:
	- Creation date
	- Due date
	- Live chat
1. We anticipate that there will be other fields for your project based upon your chosen domain.  These requirements will come as a part of your requirements elicitation.
1. When a project is deleted, all information stored in the PostgreSQL database, including title, members, description, etc., and all files stored on Amazon S3 should be deleted as well.  Projects cannot be recovered after they have been deleted.

### Anonymous User
{: .no_toc }

1. The PMA shall allow an anonymous user to view a listing of all project titles and the project's owner.  The PMA can, but is not required to, show an anonymous user other high-level information, such as description, creation date, or other domain-specific information if they are a part of the PMA design.
1. No information about the contents of a project, including files, members, messages, etc., should be visible to an anonymous user.
1. The PMA shall provide a button for an anonymous user to login to the system.

### Common User
{: .no_toc }

1. The PMA shall allow a common user to create an account in the system using their Google account.
1. When a common user creates an account, a profile should be created for the user.  A profile should consist of, at a minimum, the user's real name, the user's Google account/address, and the date they joined the PMA.  Other data, such as a profile picture, interests, description, etc. can be added based on the requirements elicitation activity.
1. A common user shall have the ability to create a new project.  When they create a new project, they automatically become the owner of the project.  See [Projects](#projects) for more information about what is needed when a project is created.
1. A common user shall have the ability to delete projects that they own, but no other projects.  
1. A common user shall have the ability to request to join a project through a button in the system on the project's description in a reasonable way.  
1. A common user shall have the ability to leave a project through a button on the project's page or on their profile page.
1. A common user that is the owner of a project shall have the ability to accept or reject a new member's request to join a project through a reasonable user interface in the PMA.
1. A common user shall have the ability to add content to a project.  This should include posting messages and uploading files.
1. A common user shall have the ability to delete files that they upload.
1. A common user shall have the ability to view all content associated with a project for which they are a member.

### PMA Administrators
{: .no_toc }

1. A PMA Administrator shall be created by having their account elevated to site admin status by a Django Admin user logging in to the Django admin site and making the change to the account there.  Only a Django Admin can grant site PMA Administrator privileges.
1. A PMA Administrator shall have the ability to see all content in the PMA, including all projects and files.
1. A PMA Administrator shall have the ability to moderate projects by deleting files or entire projects. 
1. A PMA Administrator cannot create or join projects.  

### Django Administrator
{: .no_toc }

1. A Django Administrator is created only through the `createsuperuser` Django command.
1. A Django Administrator can only access the Django admin page. No other account type should have access to the Django admin page.
1. Django Administrators have the ability to change a common user into a PMA Administrator by changing a value in the user record through the Django admin page.

## Variations and Themes
{: .no_toc }

1. Your team's app can take the requirements above and place the app in whatever domain your team is interested in.
1. Extended requirements for your app will come from the requirements elicitation activity you will in the first few weeks of class.

## Team Roles

Each member of your five person team will take on one of these roles.  Each role has different responsibilities, but ALL ROLES require that you be an active contributor to the code of the project.  In other words, if you take on Scrum Master, that doesn't mean you don't have to contribute as much code as someone else.  Please see the [information on Assessment and Grading](/syllabus.html#assessment-and-grading) for more information.

__Scrum Master__ - The Scrum Master could also be called the Team Leader, but it's not really a "leader" position, per se, in that they are not making major decisions about the project itself.  The Scrum Master is responsible for keeping everyone on track, facilitating all team meetings, and monitoring team status / issues.  The course staff will come to the Scrum Master first if there are any team issues or questions, and similarly the Scrum Master needs to know what's going on with the team and can communicate with the staff if someone is falling behind, etc.

- Reasons to be the Scrum Master: You like keeping schedules; you like keeping things organized; you don't mind being the point of contact with the staff.
- Reasons not to be the Scrum Master: You are not the most organized person; you don't think you can stay on top of what the team is working on; you don't like talking to the staff.

_Major Artifact_: [Scrum Master Final Report]({{ site.data.externallinks.scrum_master_report_template }}), due at the end of the semester   

__Requirements Manager__ - The Requirements Manager is responsible for keeping up with the features of the project.  This person will take the lead on the requirements elicitation process (which takes place in the first couple weeks of the project) as their major activity.  Note that the Requirements Manager doesn't do the whole process - they just lead the effort.  Everyone else has to participate as well!  Then throughout the semester they will manage the feature/issue tracker in GitHub, monitoring the state of the project.

- Reasons to be the Requirements Manager: You are interested in learning how requirements are created; you want to find out what your fellow students are excited about with your project; you like knowing "what's coming next" in the project.
- Reasons to not be the Requirements Manager: You have no interest in interacting with other people to find out what they want in a system; your first couple weeks of the semester are super hectic and you don't have the time for the elicitation process.

_Major Artifact_: [Requirements Elicitation Document]({{ site.data.externallinks.requirements_report_template }}), due within the first few weeks of the semester    

__Testing Manager__ - The Testing Manager is responsible for ensuring that the system is thoroughly tested, for developing the overall testing plan/philosophy of the team, and spearheading the beta testing effort at the end of the semester.  The Testing Manager is responsible for executing beta testing at the end of the semester and creating the Beta Testing Document.  The Testing Manager is also responsible for overseeing the testing philosophy throughout the semester, ensuring unit tests are being written.  Note that the Testing Manager does _not_ write every test case in the system - they just keep up with what everyone else is doing and lend support as needed.

- Reasons to be the Testing Manager: You want to learn more about testing procedures; you love seeing that unit test result bar turn green; you took HCI or something similar and are interested in setting up user testing.
- Reasons not to be the Testing Manager: You don't see the value in writing tests; you don't want to work with your fellow students in doing in-person testing.

_Major Artifact_: [Beta Testing Report]({{ site.data.externallinks.beta_testing_report_template }}), due near the end of the semester    

__DevOps Manager__ - The DevOps Manager is the support tech for the team in a sense.  They are responsible for the management and support of all the systems we are using in the class, namely GitHub, GitHub Actions, Amazon S3, and Heroku.  They should be a person that is relatively comfortable tinkering with computers and settings.  The DevOps Manager does not have to have all the answers, but would be the contact person for going to the staff to get help on any particular issues.  The DevOps Manager does need to have access to a credit card for setting up the various accounts for the team.

- Reasons to be the DevOps Manager: You are familiar with the tools mentioned already, or you are really interested in learning more about them; you like to tinker with settings to get things working "just right"; you have the patience to help those on your team who might need assistance getting their environments working.
- Reasons not to be the DevOps Manager: You do not feel comfortable helping others with technical issues; you are very unfamiliar with the tools above and would rather just have a "turnkey" solution for doing your work this semester.

_Major Artifact_: [DevOps Report]({{ site.data.externallinks.devops_report_template }}), due near the end of the semester  

__Software Architect__ - Midway through the project, a requirements change will be introduced to the base requirements listed above.  The job of the Software Architect is to determine how to implement the change, document the steps that need to be taken, and then help the team implement the change.  The Software Architect is _not_ the primary coder for the project and should not be treated as such.  

- Reasons to be the Software Architect: You enjoy solving a puzzle using critical thinking and you are interested in how software is put together.
- Reasons not to be the Software Architect: You hate troubleshooting code.

_Major Artifact_: [Requirments Change Analysis]({{ site.data.externallinks.sa_report_template }}), due after the requirements change is introduced  

__Sixth Team Member__ - If your team has 6 members, the member without a role listed above should come to office hours with the professor to discuss options.  The role will be determined based on interest and needs of the team.

__Only Four Team Members__ - If your team only has 4 members due to the number of students in the course or because a student drops, the role that should be left out is _Software Architect._  All other roles must still be filled.  A team with 4 members _does not_ have to submit the Requirements Change Analysis document, but will still implement the change.

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

### Sprint 1: {{site.data.semesterinfo.sprint_1.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_1.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_1.sprint_check}}

__Goal:__ Have your initial meeting as a team and determine who will be doing what on the team.  This meeting can be any time between when your team is formed and your sprint check meeting with your TA on the first Sunday or Monday of the sprint.  The Scrum Master of each team MUST complete this form with the team as a part of the Sprint: [Team Declaration Form]({{ site.data.externallinks.team_declaration_form }}).  Also, Scrum Masters should initialize the team GitHub repo through [GitHub Classroom]({{ site.data.externallinks.github_classroom_project }}).  Please use your assigned team number for the identifier when prompted (e.g., A-03).  Other team members can then go to that link and accept the assignment, selecting the proper team.

__Requirements and XP Allocation:__      

- 15 XP: Complete the Team Declaration form above.
- 10 XP: GitHub repo initialized and all team member accounts have joined the project.

__Team Evals:__ No Team Evals this week.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  (No, you won't have much to report this week, but think about what's coming up and discuss that.)

### Sprint 2: {{site.data.semesterinfo.sprint_2.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_2.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_2.sprint_check}}

__Goal:__ Spend most of this sprint working as a team to elicit the full requirements for your system.  Note that while the final Requirements Document is the responsibility of the Requirements Manager, _all team members_ are expected to contribute to gathering and refining the final set of requirements.  Once you have a good set of user stories / issues / tasks for your team to work on, add these as Issues to your GitHub Issues page on your team's repository.

__Requirements:__ The team must have a "reasonable" set of user stories / issues in GitHub Issues to begin with (around 10 is a lower-bound target).  We do not expect you to have your final set of features at this point.  However, you need to be able to show the TA that you have gathered requirements data and that you have converted at least some of this information into GitHub Issues.  The Requirements Manager will receive a separate score for the requirements document, which is due by the date indicated in Gradescope.  The team also needs to ensure Heroku is set up properly and that you can deploy at least the basic, default Django app.

- [Example Requirements Document from Spring 2020](https://docs.google.com/document/d/1l39MWsVEX8LWcQ16Wo5-PXyaKhfm_O6j-1Uj6wj8RUU/edit?usp=sharing)
- ["Excellent" Example from Fall 2020](https://docs.google.com/document/d/1aqeWWhA1QztrM_6iAI1PF3FjP8VTvOqCXhe5w9D9GaU/edit?usp=sharing)
- ["Great" Example from Fall 2020](https://docs.google.com/document/d/12a8MTkqiUZbnDIs-xRfmCQUb8ozs3jHamdcwp6fuqSc/edit?usp=sharing)
- ["Good" Example from Fall 2020](https://docs.google.com/document/d/1RxUBAEFjk0HpQ1aFOOX830nenFBX_Idao3vRVBYop1A/edit?usp=sharing)

__XP Allocation:__

- 15 XP: Team has populated GitHub Issues with a reasonable number of issues/features (~10 at least) that are appropriate for the project.
- 10 XP: Team can deploy the basic, default Django app to Heroku.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }})

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  Your GitHub Issues page should be populated with your team's project requirements.  (NOTE: If you would like to use GitHub Projects instead of Issues, you may do so.)  The requirements manager should submit the requirements document to the appropriate assignment by the separate due date listed.  No other team members should submit the requirements document.

### Sprint 3: {{site.data.semesterinfo.sprint_3.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_3.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_3.sprint_check}}

__Goal:__ All PMAs must have a user account feature for students to login with.  To accomplish this, you are to integrate Google login to your app.

__Requirements:__ A user with a Google Account can login to the system and the system shows in some way that that user has indeed logged in. You must show that both a Common User account _and_ a PMA Administrator account can login and that they get different screens.  Note the requirements for the different types of users above.  Print the user's name and account name to the screen to show that it works.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__XP Allocation:__

- 15 XP: Team can show that a Common User and a PMA Administrator can both login and be shown something different based upon their user role.
- 10 XP: Team worked on other features other than the Google login and is on track.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 4: {{site.data.semesterinfo.sprint_4.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_4.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_4.sprint_check}}

__Goal:__ All projects must allow a user to upload files to Amazon S3.

__Requirements:__ A major component of your system is to allow users to upload files to a permanent storage location (i.e. not directly to your Heroku installation).  Using Amazon S3, implement the necessary features to allow users to upload the three file types listed in the requirements above and show that the files can be viewed by another member of the project through the website itself (not by just going directly to S3.)  GitHub Actions CI should be operational with at least multiple test cases in order to earn full XP.  As you are just getting started with testing, this is more showing us that you have the process setup and that you have some passing tests.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__XP Allocation:__

- 15 XP: Team can demonstrate how a Common User can upload a file to the PMA and that the file can be viewed by another member of the project.
- 10 XP: Team worked on other features other than Amazon S3 and is on track.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 5: {{site.data.semesterinfo.sprint_5.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_5.duration}}    
__Sprint Due:__ {{site.data.semesterinfo.sprint_5.sprint_check}}

__Goal:__ The Software Architect takes the lead in guiding the team through the requirements change. 

__Requirements:__ At the beginning of Sprint 5, the staff will introduce a requirements change to the project.  The Software Architect is responsible for leading the team through this change and documenting the needed architectural changes to handle the update.  

__Requirments Change:__ See [Projects](https://f24.cs3240.org/project.html#projects) above.  After seeing how you handled uploading files to Amazon S3, your "customer" realized that searching through PDFs was going to be a huge headache unless they knew what they were looking for.  They want you to add the ability to add metadata to a file at upload time per the new requirement above.  The "customer" would love to see you implement a search feature based on the keywords if you have time... but they don't have the money to pay you more.

__XP Allocation:__

- 15 XP: Requirements change handled effectively.
- 10 XP: Team worked on other features other than Amazon S3 and is on track.

__Team Evals:__ At the end of Sprints 2-6 and at the end of the semester, you will need to fill out an evaluation for _each member_ of your team! You can find the evaluation form here: [Student Team Sprint Evaluations]({{ site.data.externallinks.sprint_team_evaluations }}).  Students who do not fully participate in the team evaluation process will be penalized on their final Team and Staff Evaluation score.

__How To Submit:__ Scrum Masters should fill out a [Sprint Report]({{ site.data.externallinks.sprint_report }}) and submit it to Gradescope by noon on Sunday at the completion of the sprint so they can reference it.  Scrum Masters -must- select their team members in Gradescope when submitting so all members will earn the XP for the sprint.  The main branch of your GitHub repo should be live on Heroku.

### Sprint 6: {{site.data.semesterinfo.sprint_6.goal}}

__Sprint Duration:__  {{site.data.semesterinfo.sprint_6.duration}}     
__Sprint Due:__ {{site.data.semesterinfo.sprint_6.sprint_check}}

__Goal:__ After Sprint 6 is complete, you are going to have other students test your system.  So you need a working system with most all of your functionality ready to go.  The app may not be fully polished and still needs a bit of work, but it needs to be usable from beginning to end.  Your team must be updating GitHub Issues as appropriate throughout the rest of the project.

__Requirments and Full Beta Version:__ In the opinion of the TA, you have an app that is ready for other students to test out (e.g. it doesn't crash, it looks reasonably good, it has most features, etc.).  You will earn 25 XP for the sprint check plus 100 XP as the first half of your overall project score of 250 XP (basically, if you have a working app at this point, we know your final project grade will be at least 100/250 XP, so we can give you those points now).

__XP Allocation:__

- 100 XP: Beta Version works!  App turns on and does things!  It's ready for users!
- 15 XP: PMA is nearly feature complete.
- 10 XP: User interface shows thoughtfulness on the part of the team and is ready for beta testers.

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

The final project is worth a total of 250 XP.  (100 XP will be awarded after Sprint 6 for your Beta version and the remaining 150 XP will be awarded by the professors after final demos.)  Like the other assessments in this course, grading is overall holistic - that is, there is no specific point-for-point breakdown for the rubric.  One reason for this is that this is simply not how software is delivered in real-life.  There are basically only four outcomes:

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