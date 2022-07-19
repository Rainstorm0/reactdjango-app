import React, { Component } from 'react';

export default class Navbar extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className={this.props.className}>
                <h1>Navigation Bar</h1>
            </div>
        );
    }
}
