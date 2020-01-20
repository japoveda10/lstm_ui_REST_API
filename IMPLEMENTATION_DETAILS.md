# LSTM UI Vue.js Project Implementation Details

**LSTM UI** is a **Vue.js** project. It was created using the **Vue CLI**. It has the next file structure:

```
├── babel.config.js
├── dist
├── IMPLEMENTATION_DETAILS.md
├── node_modules
├── package-lock.json
├── package.json
├── public
    ├── favicon.ico                        # Default favicon
    └── index.html                         # Main HTML file
├── README.md
└── src
    ├── App.vue                            # App component
    ├── chart-data.js                      # Example results data
    ├── components
        ├── layout                         # Layout components
            └── Header.vue
        ├── RunningCase.vue
        ├── RunningCases.vue
        ├── SelectEventLogForm.vue
        └── SelectRunningCaseForm.vue
    ├── main.js                            # Entry point
    ├── router
        └── index.js                       # Defines app's routes
    └── views
        ├── About.vue
        ├── ContactUs.vue
        ├── Home.vue
        ├── Predict.vue
        └── Results.vue
```

**Vue.js** views are built with **components**. **Components** have three main tags:

* template - HTML
* script   - JavaScript
* style    - CSS

**Components** have **Lifecycle Hooks**, like `mounted()`, that allow the developer to do specific things when a component is created, updated, deleted, etc.
