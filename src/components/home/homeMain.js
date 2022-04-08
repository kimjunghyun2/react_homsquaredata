import React from "react";
import styled from "styled-components";
import SideBanner from "../comp_public/sidebanner";
import SearchLog from "../comp_public/searchlog";




const HomeMain = () => {
    return(
        <StyledWrap>
            <p>홈메인입니다</p>
            <StyledInfo>

                <Blank/>
 
            </StyledInfo>
        </StyledWrap>

    )
}
export default HomeMain;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
`
const StyledInfo = styled.div`
    font-size: 0.875rem;
    color: #666;
    cursor: default;
    width: 15rem;
    float: right;

    & button {
        border: none;
        padding-top: 0.3rem;
        font-size: 0.875rem;
        color: #666;
        background: none;
        cursor: pointer;

        :hover {
            color: #000;
        }
    }
`
const Blank = styled.div`
    min-height: 6rem;
`