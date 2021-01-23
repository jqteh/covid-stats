import React from 'react';
import Header from './Header';
import Footer from './Footer';
import LatestCovid from './LatestCovid' //Console logs the latest Covid data from coronavirus.data.gov.uk (England for now)

function App() {


  return (
    <div className="App">
    <Header/>
    <p> something here</p>
    <LatestCovid/> 
    <Footer/>
    </div>
  );
}

export default App;
