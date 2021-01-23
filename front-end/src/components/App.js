import React, { useState } from 'react';
import Header from './Header';
import Footer from './Footer';
import LatestCovid from './LatestCovid' //Console logs the latest Covid data from coronavirus.data.gov.uk (England for now)
import VacRate from './VacRate';
import InfRate from './InfRate';
import Hospital from './Hospital';
import Sidebar from "react-sidebar";
import SidebarContent from './SidebarContent';

function App() {

  const [sideBarOpen, setSideBarOpen] = useState(false);
  const [region, setRegion] = useState("East of England");

  function showPanel() {
    setSideBarOpen(true);
  }

  function closePanel() {
    setSideBarOpen(false);
  }

  function changeRegion(place) {
    setRegion(place);
  }

  return (
    <div className="App">
        <Sidebar
          sidebar={<SidebarContent onPress={closePanel} onChangeRegion={changeRegion}/>}
          open={sideBarOpen}
          styles={{ sidebar: { background: "#1F1B2E" } }}
          pullRight={true}
        />
      <Header onPress={showPanel} />
      <div className="panel-box">
        <VacRate 
          region={region}
        />
        <InfRate />
        <Hospital />
      </div>
      <div className="risk-box">
        <h2 className="infection-risk-text">Your current risk of infection is:</h2>
        <h1 className="infection-risk">X%</h1>
      </div>
      {/* <LatestCovid/>  */}
      <Footer />
    </div>
  );
}

export default App;
