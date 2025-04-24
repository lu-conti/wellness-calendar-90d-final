# GitHub Deployment Guide for Wellness Calendar

This guide will walk you through the simple steps to deploy your Wellness Calendar to GitHub and Netlify using only the web interface (no command line needed).

## Step 1: Create a New GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in to your account
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name your repository (e.g., "wellness-calendar")
4. Make it public (unless you prefer private)
5. Skip adding README, .gitignore, or license files
6. Click "Create repository"

## Step 2: Upload All Files at Once

1. On your new empty repository page, you'll see an option to "uploading an existing file"
2. Click on this option
3. Extract the wellness calendar zip file on your computer
4. Select all files and folders inside the extracted directory
5. Drag and drop them onto the GitHub upload area
   - If you have many files, you may need to upload them in batches
   - Start with the HTML files and CSS folder
   - Then upload the data and js folders
6. Add a commit message like "Initial upload of wellness calendar"
7. Click "Commit changes"

## Step 3: Connect to Netlify

1. Go to [app.netlify.com](https://app.netlify.com) and sign in
2. Click "Add new site" → "Import an existing project"
3. Select GitHub as your Git provider
4. Find and select your new repository ("wellness-calendar")
5. In the deploy settings:
   - Build command: leave blank
   - Publish directory: leave blank (or enter "." if required)
6. Click "Deploy site"

## Step 4: Configure Your Site

1. Once deployed, click on "Site settings"
2. You can change your site name under "Site information" → "Change site name"
3. Your site will be available at `https://your-site-name.netlify.app`

## Step 5: Verify Everything Works

1. Visit your new Netlify site URL
2. Check that the calendar displays correctly
3. Verify you can navigate between days using the "Previous Day" and "Next Day" buttons
4. Confirm the exercise program tab works correctly with the home/gym toggle

## Troubleshooting

If you encounter any issues:

1. **Files not showing up**: Make sure you uploaded all files and folders
2. **Navigation not working**: Verify all HTML files were uploaded correctly
3. **Styling issues**: Ensure the CSS folder and styles.css file were uploaded
4. **Exercise program not working**: Check that all exercise HTML files were uploaded

## Making Future Updates

To update your site in the future:

1. Go to your GitHub repository
2. Navigate to the file you want to update
3. Click the pencil icon to edit the file
4. Make your changes
5. Scroll down and click "Commit changes"
6. Netlify will automatically detect the changes and redeploy your site

That's it! Your wellness calendar is now deployed and accessible from anywhere.
