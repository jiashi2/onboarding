Overview:
Our marketplace relies on having a strong volume of sellers willing to sell gift cards at a large discount.  The Seller Onboarding Form is the first thing a seller sees on landing on our site. You’ll be implementing this Form; a reference implementation is provided in [1] below.  We want the Form to be easy to use, yet collect all the info required to sell the card. 
Core Requirements (Specs):
The Seller Onboarding Form should have at least the 6 questions in the “Question Flow” section below.  Each question should be displayed alone, sequentially, like [1].
It should display completed forms in a Results Page like [2]
Don’t worry about authentication; it is OK if anyone can view the results.
It should be in Python. You are encouraged to use all nonhuman resources (Google, GPT4, etc). Please do not use human resources, and please do not share this doc.
The Results Page should display inputs even if a user doesn’t get to the form’s end
A user hitting refresh on the browser should start a new Entry (a new row in Results Page), but if the user hits back or forward with the form’s buttons, she stays within the same Entry.
Your deliverable should ideally be a page we can view on the Internet. This could be on Heroku / a small instance of DigitalOcean/AWS. Or it can be an ad-hoc setup on your local machine (e.g. could use flask or Django) that is publicly accessible.
If you’re unable to get the above to work under 1 hour, don’t worry and just zip your Django project files or Github repo. Include a README.md file that lets us run the project with minimal setup in our environment (a sandbox with WSL / Ubuntu).
Reference Implementation
We have already implemented a version of the Seller Onboarding Form at 
[1] https://agora-gcp.uc.r.appspot.com/agora/seller_intake_survey/ .  And the results display at:
[2] https://agora-gcp.uc.r.appspot.com/agora/seller_intake_survey_results/
We encourage you to play around with it for a few minutes to understand how it currently works.

Note the exercise isn’t about copying [1].  To save you time, you are not required to have some features that [1] has. These features include data validation, currency selector, drop downs, etc.  Where the Specs and [1] differ, the Specs take priority.  Also, there are areas you can optionally improve upon [1] (for example, in [1], hitting “return” on your keyboard takes you backwards).  
Question Flow Diagram: Required Questions
What is the name of your store? [Free Text Entry OK]
What is the balance left on your gift card [Free Text Entry OK]
What price are you selling at [Free Text Entry OK]
Which network would you like to receive funds at? {Polygon or Ethereum} [Ideally a selector, but free text entry OK]
What address do you want to receive funds at? [Free Text Entry]
What’s your email address? [Free Text Entry]
Note this question 6 differs from [1].  [1] goes into a more complex branch.

Once the Question Flow ends you can have a page that thanks the user.  Note that Questions 1-5 track [1] closely.

