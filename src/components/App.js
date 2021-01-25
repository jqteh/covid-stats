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
  const [currentVac, setCurrentVac] = useState(0);
  const [herdDays, setHerdDays] = useState(0);
  const [infRisk, setInfRisk] = useState(46);
  const [vacDose, setVacDose] = useState(0);

  var vacMultipler = 1;
  
  if (vacDose === 1) {
    vacMultipler = 0.48;
  } else if (vacDose === 2) {
    vacMultipler = 0.05
  } 

  const adjInfRisk = Math.round(infRisk * vacMultipler);

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

  function changeVacDose(num) {
    setVacDose(num);
  }

  useEffect(() => {

    const toBackEnd = {
      "region": region,
      "age": age,
      "wash": wash
    };

    axios.post('/api', toBackEnd)
    .then(function (response) {
      setCurrentVac(response.data["percent_vacc"][0]) 
      setHerdDays(response.data["herd_imm_days"][0])
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });

    console.log(toBackEnd)

  }, [age, region, wash])

  return (
    <div className="App">
      <Sidebar
        sidebar={<SidebarContent onPress={closePanel} onChangeRegion={changeRegion} onChangeAge={changeAge} onChangeWash={changeWash} onChangeVacDose={changeVacDose}/>}
        open={sideBarOpen}
        styles={{ sidebar: { background: "#1F1B2E" } }}
        pullRight={true}
      />
      <Header onPress={showPanel} />
      <div className="panel-box">
        <VacRate region={region} currentVac={currentVac} herdDays={herdDays}/>
        <InfRate region={region} />
        <Hospital region={region} />
      </div>
      <div className="risk-box">
        <h2 className="infection-risk-text">Your risk of infection in 30 days is:</h2>
        <h1 className="infection-risk">{adjInfRisk}%</h1>
        <LatestCovid region={region} />
      </div>
      {/* <button onClick={() => { console.log(currentVac) }}>check</button> */}
      <Footer />
    </div>
  );
}

export default App;
