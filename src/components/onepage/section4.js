//section4 클릭시 모달
//section5 자세히 보기 하이퍼링크
import React from "react";
import styled from "styled-components";


const Section4 = () => {
    return(
        <StyledMargin>
        <StyledWrap>
            <Section4Style>
            <p>섹션4</p>
            </Section4Style>
            <Section5Style>
            <p>섹션5</p>
            </Section5Style>
        </StyledWrap>
        </StyledMargin>
    )
}
export default Section4;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;

    `

const Section4Style = styled.div`
    height: 105px;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_4.png");
    `

const Section5Style = styled.div`
    height: 235px;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_5.png");
`

const Section6Style = styled.div`
    height: 150px;
    margin: 0 auto;
    text-align: center;
    background-size: contain;
    background-repeat: no-repeat;
    background-image: url("/img/refimg_6.png");
`


const Blank = styled.div`
    min-height: 3rem;
    `
    const StyledMargin = styled.div`
    margin: 0 auto;
    padding: 1rem 0;
    background-color: #fefefe;
`