import React, { Component } from 'react';
import { render } from 'react-dom';

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (<React.Fragment>
            <h1>Successful react init</h1>
        </React.Fragment>);
    }
}
