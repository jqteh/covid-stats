import React from 'react';
import Header from './Header';
import Footer from './Footer';
import LatestCovid from './LatestCovid' //Console logs the latest Covid data from coronavirus.data.gov.uk (England for now)
import VacRate from './VacRate';
import InfRate from './InfRate';
import Hospital from './Hospital';

function App() {


  return (
    <div className="App">
    <Header/>
      <div className="panel-box">
        <VacRate/>
        <InfRate/>
        <Hospital/>
      </div>
      <div className="risk-box">
        <h2 className="infection-risk-text">Your current risk of infection is:</h2>
        <h1 className="infection-risk">X%</h1>
      </div>
    {/* <LatestCovid/>  */}
    <Footer/>
    </div>
  );
}

export default App;
