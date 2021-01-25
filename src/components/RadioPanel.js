import React, { useState } from 'react';
import Radio from '@material-ui/core/Radio';
import RadioGroup from '@material-ui/core/RadioGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';


export default function RadioPanel(props) {

    const [selectedValue, setSelectedValue] = useState("0");

    const handleChange = (event) => {
        const newValue = event.target.value
        setSelectedValue(newValue);
        props.endValue(newValue);
    };

    return (
        <FormControl component="fieldset">
            <RadioGroup row aria-label="position" name="position" defaultValue="top">
                <FormControlLabel
                    value="0"
                    control={<Radio color="primary" />}
                    label="0"
                    labelPlacement="top"
                    onChange={handleChange}
                />
                <FormControlLabel
                    value="1"
                    control={<Radio color="primary" />}
                    label="1"
                    labelPlacement="top"
                    onChange={handleChange}
                />
                <FormControlLabel
                    value="2"
                    control={<Radio color="primary" />}
                    label="2"
                    labelPlacement="top"
                    onChange={handleChange}
                />
            </RadioGroup>
        </FormControl>
    )
}
