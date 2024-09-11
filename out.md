```public/index.html
   1 | <!DOCTYPE html>
   2 | <html lang="en">
   3 |   <head>
   4 |     <meta charset="utf-8" />
   5 |     <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
   6 |     <meta name="viewport" content="width=device-width, initial-scale=1" />
   7 |     <meta name="theme-color" content="#000000" />
   8 |     <meta
   9 |       name="description"
  10 |       content="Web site created using create-react-app"
  11 |     />
  12 |     <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
  13 |     <!--
  14 |       manifest.json provides metadata used when your web app is installed on a
  15 |       user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
  16 |     -->
  17 |     <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
  18 |     <!--
  19 |       Notice the use of %PUBLIC_URL% in the tags above.
  20 |       It will be replaced with the URL of the `public` folder during the build.
  21 |       Only files inside the `public` folder can be referenced from the HTML.
  22 | 
  23 |       Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
  24 |       work correctly both with client-side routing and a non-root public URL.
  25 |       Learn how to configure a non-root public URL by running `npm run build`.
  26 |     -->
  27 |     <title>React App</title>
  28 |   </head>
  29 |   <body>
  30 |     <noscript>You need to enable JavaScript to run this app.</noscript>
  31 |     <div id="root"></div>
  32 |     <!--
  33 |       This HTML file is a template.
  34 |       If you open it directly in the browser, you will see an empty page.
  35 | 
  36 |       You can add webfonts, meta tags, or analytics to this file.
  37 |       The build step will place the bundled scripts into the <body> tag.
  38 | 
  39 |       To begin the development, run `npm start` or `yarn start`.
  40 |       To create a production bundle, use `npm run build` or `yarn build`.
  41 |     -->
  42 |   </body>
  43 | </html>
```

```src/reportWebVitals.js
   1 | const reportWebVitals = onPerfEntry => {
   2 |   if (onPerfEntry && onPerfEntry instanceof Function) {
   3 |     import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
   4 |       getCLS(onPerfEntry);
   5 |       getFID(onPerfEntry);
   6 |       getFCP(onPerfEntry);
   7 |       getLCP(onPerfEntry);
   8 |       getTTFB(onPerfEntry);
   9 |     });
  10 |   }
  11 | };
  12 | 
  13 | export default reportWebVitals;
```

```src/App.css
   1 | .App {
   2 |   text-align: center;
   3 | }
   4 | 
   5 | .App-logo {
   6 |   height: 40vmin;
   7 |   pointer-events: none;
   8 | }
   9 | 
  10 | @media (prefers-reduced-motion: no-preference) {
  11 |   .App-logo {
  12 |     animation: App-logo-spin infinite 10s linear reverse;
  13 |   }
  14 | }
  15 | 
  16 | .App-header {
  17 |   background-color: #135713;
  18 |   min-height: 100vh;
  19 |   display: flex;
  20 |   flex-direction: column;
  21 |   align-items: center;
  22 |   justify-content: center;
  23 |   font-size: calc(10px + 2vmin);
  24 |   color: #90EE90;
  25 | }
  26 | 
  27 | .App-link {
  28 |   color: #00FF00;
  29 | }
  30 | 
  31 | @keyframes App-logo-spin {
  32 |   from {
  33 |     transform: rotate(0deg);
  34 |   }
  35 |   to {
  36 |     transform: rotate(360deg);
  37 |   }
  38 | }
  39 | 
```

```src/index.js
   1 | import React from 'react';
   2 | import ReactDOM from 'react-dom/client';
   3 | import './index.css';
   4 | import App from './App';
   5 | import reportWebVitals from './reportWebVitals';
   6 | 
   7 | const root = ReactDOM.createRoot(document.getElementById('root'));
   8 | root.render(
   9 |   <React.StrictMode>
  10 |     <App />
  11 |   </React.StrictMode>
  12 | );
  13 | 
  14 | // If you want to start measuring performance in your app, pass a function
  15 | // to log results (for example: reportWebVitals(console.log))
  16 | // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
  17 | reportWebVitals();
```

```src/index.css
   1 | body {
   2 |   margin: 0;
   3 |   font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
   4 |     'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
   5 |     sans-serif;
   6 |   -webkit-font-smoothing: antialiased;
   7 |   -moz-osx-font-smoothing: grayscale;
   8 | }
   9 | 
  10 | code {
  11 |   font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
  12 |     monospace;
  13 | }
```

```src/App.test.js
   1 | import { render, screen } from '@testing-library/react';
   2 | import App from './App';
   3 | 
   4 | test('renders learn react link', () => {
   5 |   render(<App />);
   6 |   const linkElement = screen.getByText(/learn react/i);
   7 |   expect(linkElement).toBeInTheDocument();
   8 | });
```

```src/setupTests.js
   1 | // jest-dom adds custom jest matchers for asserting on DOM nodes.
   2 | // allows you to do things like:
   3 | // expect(element).toHaveTextContent(/react/i)
   4 | // learn more: https://github.com/testing-library/jest-dom
   5 | import '@testing-library/jest-dom';
```

```src/App.js
   1 | import logo from './logo.svg';
   2 | import './App.css';
   3 | 
   4 | function App() {
   5 |   return (
   6 |     <div className="App">
   7 |       <header className="App-header">
   8 |         <img src={logo} className="App-logo" alt="logo" />
   9 |         <p>
  10 |           Edit <code>src/App.js</code> and save to reload.
  11 |         </p>
  12 |         <a
  13 |           className="App-link"
  14 |           href="https://reactjs.org"
  15 |           target="_blank"
  16 |           rel="noopener noreferrer"
  17 |         >
  18 |           Learn React
  19 |         </a>
  20 |       </header>
  21 |     </div>
  22 |   );
  23 | }
  24 | 
  25 | export default App;
```

