import React from "react";
import styled from "styled-components";


const Section7 = () => {
    return(
        <StyledMargin>
        <StyledWrap>
            <Blank/>
            <Section6Style>
            <p>섹션6</p>
            </Section6Style>
            <Section7Style>
            <p>섹션7</p>
            </Section7Style>
        </StyledWrap>
        </StyledMargin>
    )
}
export default Section7;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: auto;
    `
const Blank = styled.div`
    min-height: 3rem;
    `
    const StyledMargin = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #f0f0f0;
`
const Section6Style = styled.div`
    height: 150px;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_6.png");
`
const Section7Style = styled.div`
    height: 585px;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_7.png");
`