import React, { useState } from 'react';
import GoogleButton from './GoogleButton';
import FacebookButton from './FacebookButton';
import { GiPriceTag } from "react-icons/gi"; 

import '../style/NavBar.css';

export default function NavBar() {
    
  return (
    <nav className="navbar">
      <h1 className="logo">
        InstaPrice
        <GiPriceTag />
      </h1> 
      <div class="loginButtons">
        <GoogleButton />
        <FacebookButton />
      </div>
    </nav>
  );
}