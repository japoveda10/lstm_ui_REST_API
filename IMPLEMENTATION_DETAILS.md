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
    ├── favicon.ico                # Default favicon
    └── index.html                 # Main HTML file
├── README.md
└── src
    ├── App.vue                    # App component
    ├── chart-data.js              # Example results data
    ├── components
        ├── layout                 # Layout components
            └── Header.vue
        ├── RunningCase.vue
        ├── RunningCases.vue
        ├── SelectEventLogForm.vue
        └── SelectRunningCaseForm.vue
    ├── main.js
    ├── router
        └── index.js
    └── views
        ├── About.vue
        ├── ContactUs.vue
        ├── Home.vue
        ├── Predict.vue
        └── Results.vue
```

Vue.js have **components**. Components have three main tags:

* <template></template>     - HTML
* <script></script>         - JS  
* <style scoped></style>    - CSS
