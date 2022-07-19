import React, { Component } from 'react';
import Navbar from './Navbar';
import Calendar from './Calendar';

export default class App extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <React.Fragment>
            <Navbar className="Navbar"/>
            <Calendar/>
        </React.Fragment>);
    }
}
