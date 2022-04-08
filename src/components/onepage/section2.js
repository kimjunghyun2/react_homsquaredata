import React from "react";
import styled from "styled-components";


const Section2 = () => {
    return(
        <StyledMargin>
        <StyledWrap>
            <Blank/>
            <p>섹션2</p>
        </StyledWrap>
        </StyledMargin>
    )
}
export default Section2;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_2.png");
    height: 390px;
    `
const Blank = styled.div`
    min-height: 3rem;
    `
    const StyledMargin = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #fefefe;
`