import React from 'react';
import ReactDOM from 'react-dom';
import DiscreatSlider from './DiscreatSlider';
import MyComponent from './MyComponent';
import { Streamlit } from "streamlit-component-lib";

const rootElement = document.getElementById('root');
const componentName = rootElement?.getAttribute("data-component-name");

if (componentName === "DiscreatSlider") {
  ReactDOM.render(
    <React.StrictMode>
      <DiscreatSlider />
    </React.StrictMode>,
    rootElement
  );
} else if (componentName === "MyComponent") {
  ReactDOM.render(
    <React.StrictMode>
      <MyComponent />
    </React.StrictMode>,
    rootElement
  );
}

Streamlit.setComponentReady();
Streamlit.setFrameHeight();
