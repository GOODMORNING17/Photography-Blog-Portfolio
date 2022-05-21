Distinctiveness and Complexity:
I believe that my project has satisfied the distinctiveness and complexity requirements as my project is totally different from the other projects in this course. My project is a photography portfolio / blog website. It is also more complex as it has a contact form which is not being used in the other projects. My contact form allows for visitors to input their information so that I can receive their contact information for future collaboration and business operations. Moreover, my web application has utilized Django on the back-end and Javascript on the front-end. Moreover, my web application is also mobile-responsive.

My 'photography blog' file contains numerous files. In the views.py file, I had the index and about page defined and linked to my html. For the listings of my pictures, i had to import Listings, Category from the models.py so that i was able to get the category id and listing id. This enables me to posts pictures on my admin page and the listings from the admin will be visible on my web application. Lastly, the creation of a contact form for my 'contact' page. 

Moving on to the urls.py, this is where I place my urls and linked my urls to the htmls via the view.py file.

On the models.py, I had class of Listings, category and Contact. This is to put inputs for my listing , category and contact page. This also allows me to sync data to my sql database and see them in the Django admin page. In addition, allows me to make changes to the listing of my pictures and category. Moreover, allows me to check who has contacted me using the contact form. 

On the admin.py, I registered the Lisiting, Category, Pictures and Contact Class from the models.py page. This allows me to make changes and see information via the Django admin page.

In the templates, I had an about.html file which is for my about page. contact.html file is for the Contact form so that collaborators can send me their contact information. contactfailure.html is for the red alert banner at the top when someone inputs the contact form incorrectly or forgots to input his/her details. contactsuccess.html is for the green alert banner at the top when someone successfully sends the contact form. index.html is for the homepage at the front with a large background photo which is one of my favourite photos to start my page off with a beautiful sunset. layout.html is for the navigation bar and logo at the top which is fixed on every page and can be used to access other pages too. Lastly, listing.html is a page to put my pictures and label them. There is also a category below the navigation bar to switch between the different categories like landscape, street and film. Moreover, i have also inputted a javscript to my listing page using these measures are used to determine whether or not the user has scrolled to the end of a page using the comparison window.scrollY + window.innerHeight >= document.body.offsetHeight. My page will change the backgroud color to blue when we reach the bottom of a page. 
window.scrollY: How many pixels we have scrolled from the top of the page
document.body.offsetHeight: The height in pixels of the entire document.

In the static, there is backgroundphoto2.jpg which is my background photo i used in the index page and max.jpg which is the photo I used in the about page. stylo.css is to style my page. 

My application is run via the use of 'python3 manage.py runserver'

That will be all for my web application. Hope my website is easy to use and useful for those who need a photography portfoliio/blog website. Thank you!
