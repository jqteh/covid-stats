import React, { useState, useEffect } from 'react';
import Header from './Header';
import Footer from './Footer';
import LatestCovid from './LatestCovid' //Console logs the latest Covid data from coronavirus.data.gov.uk (England for now)
import VacRate from './VacRate';
import InfRate from './InfRate';
import Hospital from './Hospital';
import Sidebar from "react-sidebar";
import SidebarContent from './SidebarContent';
import axios from 'axios';


function App() {

  const [sideBarOpen, setSideBarOpen] = useState(false);
  const [region, setRegion] = useState("East of England");
  const [age, setAge] = useState(20);
  const [wash, setWash] = useState(3);

  function showPanel() {
    setSideBarOpen(true);
  }

  function closePanel() {
    setSideBarOpen(false);
  }

  function changeRegion(place) {
    setRegion(place);
  }

  function changeAge(num) {
    setAge(num);
  }

  function changeWash(num) {
    setWash(num);
  }

  useEffect(() => {

    const toBackEnd = {
      "region": region,
      "age": age,
      "wash": wash
    };

    axios.post('/api', toBackEnd)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });

    // fetch('/api', {
    //   method: 'POST',
    //   body: toBackEnd
    // }).then(
    //   res => res.json()
    // ).then(
    //   data => console.log(data)
    // );

    console.log(toBackEnd)

  }, [age, region, wash])

  return (
    <div className="App">
      <Sidebar
        sidebar={<SidebarContent onPress={closePanel} onChangeRegion={changeRegion} onChangeAge={changeAge} onChangeWash={changeWash} />}
        open={sideBarOpen}
        styles={{ sidebar: { background: "#1F1B2E" } }}
        pullRight={true}
      />
      <Header onPress={showPanel} />
      <div className="panel-box">
        <VacRate region={region} />
        <InfRate region={region} />
        <Hospital region={region} />
      </div>
      <div className="risk-box">
        <h2 className="infection-risk-text">Your current risk of infection is:</h2>
        <h1 className="infection-risk">X%</h1>
        <LatestCovid region={region} />
      </div>
      <button onClick={() => { console.log("pressed") }}>check</button>
      <Footer />
    </div>
  );
}

export default App;
