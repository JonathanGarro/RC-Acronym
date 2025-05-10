# React Frontend for Acronym Manager

This directory contains the React frontend for the Acronym Manager Django project.

## Setup

1. Make sure you have Node.js and npm installed on your system.

2. Install the dependencies:
   ```
   cd frontend
   npm install
   ```

## Development

To build the React app in development mode with watch mode enabled:
```
npm run dev
```

This will automatically rebuild the app whenever you make changes to the source files.

## Production Build

To build the React app for production:
```
npm run build
```

## Structure

- `src/index.js`: Entry point for the React app
- `src/components/`: Directory containing React components
  - `App.js`: Main component that renders the search interface
  - `SearchBrowsePill.js`: Component for the pill navigation
  - `SearchBar.js`: Component for the search functionality

## Integration with Django

The webpack configuration outputs the bundled JavaScript to `../static/frontend/main.js`, which is then included in the Django template using the `{% static %}` template tag.

The React app is rendered in the `<div id="react-app"></div>` element in the home.html template.