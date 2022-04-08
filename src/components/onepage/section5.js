import React from "react";
import styled from "styled-components";


const Section5 = () => {
    return(
        <StyledMargin>
        <StyledWrap>
            <Blank/>
            <p>섹션5</p>
        </StyledWrap>
        </StyledMargin>
    )
}
export default Section5;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_5.png");
    height: 235px;
    `
const Blank = styled.div`
    min-height: 3rem;
    `
    const StyledMargin = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #efefef;
`