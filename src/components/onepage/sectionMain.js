import React from "react";
import styled from "styled-components";


const SectionMain = () => {
    return(
        <StyledWrap>
            <Blank/>
            <p>전월세 안전진단기능</p>
        </StyledWrap>
    )
}
export default SectionMain;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
    `
const Blank = styled.div`
    min-height: 3rem;
    `