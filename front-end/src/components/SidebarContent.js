import React, {useState} from 'react';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import SliderComponent from './SliderComponent';
import RadioPanel from './RadioPanel';
import Region from './Region';

export default function SidebarContent(props) {

    const [age, setAge] = useState(20)
    const [wash, setWash] = useState(3)
    const [vacDose, setVacDose] = useState(0)

    function setAgeValue(num){
        setAge(num);
    }

    function setWashValue(num){
        setWash(num);
    }

    function setVacDoseValue(value) {
        const num = parseInt(value)
        setVacDose(num);
    }

    return (
        <div className="sidebar-content">
            <div className="sidebar-x">
                <IconButton onClick={() => { props.onPress() }}>
                    <CloseIcon style={{ fill: "white", fontSize: "4rem"}} />
                </IconButton>
            </div>
            <h4>Find out how to reduce your risk of infection by adjust the following... </h4>
            <SliderComponent
                title="How old are you? (years)"
                max="100"
                defaultNum="20"
                endValue={setAgeValue}
            />
            <p>What is the first 2 letters of your postcode? (e.g. CB)</p>
            <Region/>
            <SliderComponent
                title="How often do you wash your hands in a day?"
                max="20"
                defaultNum="3"
                endValue={setWashValue}
            />
            <p>How many doses of vaccine have you received?</p>
            <RadioPanel
                endValue={setVacDoseValue}
            />
            <br/>
            <button onClick={()=>{console.log(age, wash, vacDose)}}>check value</button>
        </div>
    )
}
