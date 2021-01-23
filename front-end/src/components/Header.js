import React from "react";
import Logo from '../assets/logo.png';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

function Header(props) {

  return (
    <header>
    <div className="header-text">
        <img src={Logo} alt=""/>
        <h1>covidstats</h1>
        <p>Welcome to Covidstats - your one stop platform towards understanding the covid situation within the UK and your respective regions. This platform aims to provide the latest details on COVID to help you understand the severity of COVID within your own vicinity - so that you are readily equipped with your masks and vaccines to stay healthy during this time. </p>
    </div>
    <IconButton onClick={()=>{props.onPress()}}>
      <MenuIcon style={{fill: "white",fontSize:"4rem", position:"relative", marginRight:0}}/>
    </IconButton>
    </header>
  );
}

export default Header;