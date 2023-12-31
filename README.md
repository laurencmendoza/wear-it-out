# Wear It Out
'Wear It Out' is a full-stack, full CRUD application made with Django that will allow a user to log all of their clothing items, as well as track their outfits. Users can add a clothing item to their virtual closet, and then create outfits from their clothing items. Then, users can create an entry for each day to track their outfits. 

This application was created as a way for users to visualize their closet in a way that their real-life storage may not always allow. Instead of tearing apart their closet to experiment with new combinations of clothing items, this application allows users to plan out outfits and test combinations without the hassle of pulling the item out of storage. Users can keep track of what they wear regularly, and check what they wore in the past to get a better picture of their wardrobe utilization. 

## Getting Started
### [Click here to use the application!](https://wear-it-out-e8cbd3eb7d9e.herokuapp.com/)

Check out [my planning docs](https://github.com/laurencmendoza/wear-it-out/blob/main/planning.md) to see the application's user stories, wireframes, and ERD.

## Screenshots
#### Home Page (logged out view)
![Home page logged out view](https://github.com/laurencmendoza/wear-it-out/assets/137251999/7072e6a1-f8d6-450c-96a7-d2b292c6e403)

#### Home Page (logged in view)
Each item links to a list of clothing items in that category (ex: clicking on the shirt sends you to a page with all of the Tops in your closet)

![Home page logged in view](https://github.com/laurencmendoza/wear-it-out/assets/137251999/55e5c644-2bdc-4627-bba9-2cb8430c1b32)

#### Add to Closet Page - add a new clothing item to closet
![Add to closet page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/914fd254-c39b-44c8-abab-b9128074abd1)

#### My Closet Page - list of clothing items
Click on each item to view the clothing item's details, and view the first image uploaded for each clothing item (or a placeholder based on the item's category if no image is uploaded)

![My closet page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/ea656ef6-7e5c-4038-9933-748b04ec000e)

#### Clothing Item details page
Add and remove colors and tags associated with clothing item, upload photos, edit or delete

![Clothing item details page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/67309ad4-6980-4070-9de9-b3898a8a6ff3)

#### Outfits page - list of outfits created
Click on each item to view the outfit's details, view the image uploaded for each outfit (or a placeholder image if no image is uploaded), click the sun icon to check the weather, and click 'Add a New Outfit' to add to the list.

![Outfit list page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/15e1c96d-0f47-4498-b701-ff8207c2cdb1)

#### Weather - get the weather for your zip code
![Weather page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/5d31921b-ede3-421c-8bf3-9e26350e5b7c)


#### Add a New Outfit page - create a new outfit, starting with the description
![New outfit form](https://github.com/laurencmendoza/wear-it-out/assets/137251999/1bacd568-01be-406a-9f6d-d62280e91281)


#### Outfit details page
Add and remove clothing items associated with the outfit, upload photos, edit or delete

![Outfit details page 1](https://github.com/laurencmendoza/wear-it-out/assets/137251999/7ad47d9f-7610-4552-9eed-685ac3176c80)
![Outfit details page 2](https://github.com/laurencmendoza/wear-it-out/assets/137251999/8a948599-f1d4-4f10-8517-af4c2838044b)

#### Outfit Tracker page - list of entries created
Edit or delete the entry, or click on each item to view/edit the outfits associated with the entry. If an outfit is associated with the entry, preview the image uploaded to the outfit. 

![Outfit tracker page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/7edc05a6-d098-4409-b4e7-f7ccda2f5e58)

#### New Entry page - create a new entry in the outfit tracker
![New entry page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/d8ddcba5-7a23-4439-8e93-5febb9c4088a)

#### Entry details page
Add and remove outfits worn on that day

![Entry details page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/f5bba650-fea0-4e46-837c-564568ee9ab2)

#### Confirm delete page (included for clothing items, outfits, and entries in the outfit tracker)
![Confirm delete page](https://github.com/laurencmendoza/wear-it-out/assets/137251999/5de40a4f-d5ee-44ee-9463-3ec03542f950)


## Technologies Used
- Django
- [Tailwind CSS](https://tailwindcss.com/)
- [Tailwind UI](https://tailwindui.com/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api)
  
## Key Resources
1. [Django Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)
2. [Tailwind UI Navbar](https://tailwindui.com/components/application-ui/navigation/navbars)
3. [Tailwind Documentation](https://tailwindcss.com/docs/installation)
4. [Canva Logos](https://www.canva.com/logos/)
5. [Visual Crossing Weather API Docs](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/)
6. [How to Build a Weather App in Django](https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django)
7. [ColorDesigner.io](https://colordesigner.io/gradient-generator)


## Inspiration
1. [Poshmark](https://poshmark.com/)

## Current User Flow / Feature List
1. User signs up for the application or logs in using their username and password
2. User is unable to view pages such as 'My Closet', 'Outfits' and 'Outfit Tracker', and only has access to their clothing items, outfits, and entries. User is unable to add other users' clothing items to their outfits, and user is unable to access other users' outfis to add to their entries. 
3. User navigates to the home page to see a menu that allows them to view their clothing items by category by clicking on the image that corresponds to the category (ex: clicking on the shirt sends users to a list of their Tops)
4. User clicks on 'My Closet' to view all of their clothing items
5. User clicks 'Add to Closet' to add a new clothing item to the app
6. User views a detail page for the clothing item and adds/removes colors and tags (ex: casual, activewear, business attire) for the item (also available by clicking on the clothing item in the clothing item list view)
7. User can upload photos of the clothing item
8. User can edit the clothing item's information
9. User can click delete to view a confirm deletion page, and then delete the clothing item
10. User clicks on 'Outfits' to view a list of all their outfits
11. User can click on the sun icon to check the weather for their zip code
12. User clicks on 'Add a New Outfit' on the 'Outfits' page to create a new outfit, first by writing a description
13. User views a detail page for the outfit and adds/removes clothing items (also available by clicking on the outfit in the outfit list view)
14. User can upload photos of the outfit
15. User can edit the outfit description
16. User can click delete to view a confirm deletion page, and then delete the outfit
17. User clicks 'Outfit Tracker' to view a list of all of their created entries
18. User can click edit to update the description or date for each entry
19. User can click delete to view a confirm deletion page, and then delete the entry
20. User clicks on 'New Entry' on the 'Outfit Tracker' page to create a new entry, first by writing the date and a description of the day
21. User views a detail page for the entry and adds/removes outfits

## Future Features
1. User is able to create their own colors and tags for clothing items on the clothing item details page
2. On the outfit details page, user can toggle between categories (Tops, Bottoms, etc.) while selecting clothing items to add to the outfit
3. On the outfit details page, user is able to view the dates that the outfit was worn
4. On the clothing item details page, user is able to view the dates that the clothing item was worn
5. Google Custom Search API allows users to add photos of clothing items or outfits if user does not upload a photo
6. User can filter clothing items by color and tags
7. User can view entries on a calendar display, and click on dates in the calendar to add or update an entry, and track outfits worn on that day
8. User can customize the home page menu clothing items (ex: choose a dress or a suit for the icon that leads to the clothing items in the 'Full Body' category)
9. User can view photos uploaded for clothing items and outfits in a photo carousel on the details page
10. User can delete photos uploaded for clothing items and outfits
11. User can favorite clothing items and outfits for easy access while creating a new outfit or new entry, respectively
12. User can view clothing items and outfits in order of most to least worn
13. User can view all clothing items that have not been worn (based on whether the clothing item has been used in the outfit, and whether the outfit has been used in an entry in the outfit tracker)

## Known Issues
1. Missing mobile responsiveness on form pages

