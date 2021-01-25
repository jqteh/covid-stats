import React, { useState } from 'react';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import SliderComponent from './SliderComponent';
import RadioPanel from './RadioPanel';
import Region from './Region';

export default function SidebarContent(props) {

    const [age, setAge] = useState(20)
    const [wash, setWash] = useState(3)
    const [vacDose, setVacDose] = useState(0)
    const [region, setRegion] = useState("East of England")

    function setAgeValue(num) {
        setAge(num);
        props.onChangeAge(num);
    }

    function setWashValue(num) {
        setWash(num);
        props.onChangeWash(num);
    }

    function setVacDoseValue(value) {
        const num = parseInt(value)
        setVacDose(num);
        props.onChangeVacDose(num);
    }

    function setRegionValue(region) {
        setRegion(region);
        props.onChangeRegion(region);
    }

    return (
        <div className="sidebar-content">
            <div className="sidebar-x">
                <IconButton onClick={() => { props.onPress() }}>
                    <CloseIcon style={{ fill: "white", fontSize: "4rem" }} />
                </IconButton>
            </div>
            <h4>Find out how to reduce your risk of infection by adjust the following... </h4>
            <p>What is the first 2 letters of your postcode? (e.g. CB)</p>
            <Region
                endValue={setRegionValue}
            />
            <br />
            <SliderComponent
                title="How old are you? (years)"
                max="100"
                defaultNum="20"
                endValue={setAgeValue}
            />
            <br />
            <SliderComponent
                title="How often do you wash your hands in a day?"
                max="20"
                defaultNum="3"
                endValue={setWashValue}
            />
            <br />
            <p>How many doses of vaccine have you received?</p>
            <RadioPanel
                endValue={setVacDoseValue}
            />
            <br />
            {/* <button onClick={()=>{console.log(age, wash, vacDose, region)}}>check value</button> */}
        </div>
    )
}
