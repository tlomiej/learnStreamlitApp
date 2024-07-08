import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Slider from "@material-ui/core/Slider"
import styled from "styled-components"


const options = ["test1", "tets2", "test3"]

const createMarks = (labels: string[]) => {
  return labels.map((label, i) => {
    return { value: i, label }
  })
}

class DiscreatSlider extends StreamlitComponentBase<any> {
  public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {
    const hMargin = 20

    const StyledSlider = styled(Slider)({
      background:'white',
      margin: `10px 0px`,
      
      width: this.props.width - hMargin * 2,
    })

    return (
      <StyledSlider
        defaultValue={0}
        valueLabelDisplay="off"
        step={null}
        marks={createMarks(options)}
        min={0}
        max={options.length - 1}
      />
    )
  }
}

export default withStreamlitConnection(DiscreatSlider)
