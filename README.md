# DevRecruitBackend
A web application for selling and buying products within a small community.

## Hosted at
https://iitd-bazaar.herokuapp.com/

## Features
- Users can add products.
- Products are then staged for approval with the moderation. Unmoderated products don't show on any page by default. Viewers can choose to view the unmoderated products.
- Moderator can either approve or disapprove the product, and give a comment
  - On approval, the product appears on all product pages and unmoderated warning is removed from its page
  - On disapproval, the product disappears from all the pages and is only visible to the person who added it. He can then act on the review given by the moderation and edit the product details to make it acceptable.
- Users can edit the products added by them
- Products can currently be bought by contacting the sellers directly
- The products also have a category and any viewer can view products by category.
- Categories are hierarchical and breadcrumbs are displayed on each relevant page.

## Technical Features
- URL design
  - URLs are designed so as to be as human-readable as possible
  - URLs for product, user and category pages are of the form <hash>/<slug> where hash is a string of 6 or more characters that uniquely identify the page and slug is a human readable string. 
    - The application only relies on hash to fetch the page. If the slugs don't match, the user gets redirected to the page with the correct slug with a 301 redirect (moved permanently). This has an advantage of easily allowing the product title, category name to be changed (on which the slug is based on) without invalidating the previous links.
- Database design
  - We have the following models:
    - CustomUser
    - Category
    - Product
    - Images 
    - Transaction (not used currently)
  
  !['Database diagram'](https://imgur.com/tPaIS6U.png)
  
 ## Current Known Bugs and Problems
 - [#13](https://github.com/arpit-saxena/DevRecruitBackend/issues/13): Currently, images are not supported by the hosted app as Heroku doesn't support it and S3 wasn't configured properly
 - No Payment system
 
 ## Contributing
 Create a fork and a pull request, or raise an issue. Also, look at the current issues
