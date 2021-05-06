# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Project Template Setup

### Boilerplate

```console
yarn create react-app ui --template typescript
cd ui
yarn add tailwindcss@npm:@tailwindcss/postcss7-compat @tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9
yarn add @craco/craco
```

edit scripts section in package.json

```json
  "scripts": {
-   "start": "react-scripts start",
-   "build": "react-scripts build",
-   "test": "react-scripts test",

+   "start": "craco start",
+   "build": "craco build",
+   "test": "craco test",
  }

```

add craco.config.js

```console
touch craco.config.js
```

```javascript
module.exports = {
  style: {
    postcss: {
      plugins: [require("tailwindcss"), require("autoprefixer")],
    },
  },
};
```

generate tailwind.config.js

```console
yarn tailwindcss init
```

edit module.exports section in tailwind.config.css

```javascript
  module.exports = {
-   purge: [],
+   purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  }
```

replace the contents of ./src/index.css

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

check that ./src/index.tsx imports ./index.css

```typescript
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
```

replace App.tsx to check if tailwind is installed correctly

```typescript
import "./App.css";

function App() {
  return (
    <div className="min-h-screen bg-gray-200 flex justify-center items-center">
      <div className="max-w-2xl bg-white border-2 border-gray-300 p-5 rounded-md tracking-wide shadow-lg">
        <div id="header" className="flex">
          <img
            alt="mountain"
            className="w-45 rounded-md border-2 border-gray-300"
            src="https://picsum.photos/seed/picsum/200"
          />
          <div id="body" className="flex flex-col ml-5">
            <h4 id="name" className="text-xl font-semibold mb-2">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit
            </h4>
            <div id="job" className="text-gray-800 mt-2">
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
              nisi ut aliquip ex ea commodo consequat.
            </div>
            <div className="flex mt-5">
              <img
                alt="avatar"
                className="w-6 rounded-full border-2 border-gray-300"
                src="https://picsum.photos/seed/picsum/200"
              />
              <div className="ml-3">John Doe</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
```

```console
yarn start
```

### Structure

```console
mkdir ./src/components
mkdir ./src/images
mkdir ./src/pages
```

### Add other dependencies (routing, ...)

**NOTE** @zilliqa-js/core requires node yarn add @zilliqa-js/core
so...

```console
nvm install 14.16.0
nvm use 16.16.0
yarn add @zilliqa-js/core
yarn add @zilliqa-js/zilliqa
yarn add tslib
yarn add bn.js
```

```console
yarn add react-router-dom
yarn add @types/react-router-dom
yarn add @windmill/react-ui

```

modify index.tsx - import BrowserRouter & wrap App in "BrowserRouter"

```typescript
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

### Modal dialog configuration requirements

The modal dialog requires that index.html has a div "root-modal" at the root-level

```html
<div id="root"></div>
<div id="root-modal"></div>

```

### Toast package requirements

```console
 yarn add react-toast-notifications
 ```

Wrap the App in the ToastProvider, which provides context for the Toast descendants.
Modify index.tsx

```html
ReactDOM.render(
  <React.StrictMode>
    <ToastProvider>
      <App />
    </ToastProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
```

## Available Scripts

In the project directory, you can run:

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `yarn test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
