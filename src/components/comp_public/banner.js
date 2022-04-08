//광고 배너 기능에 해당 단 img는 그때 그때 달라질 수 있음 
import React from "react";
import styled from "styled-components";


const Banner = () => {
    return(
        <StyledWrap>
            <Blank/>
            <BannerStyle>
            <p>배너입니다. 실사용시에는 없어야 합니다 swipper로 구현할 수도 있습니다.</p>
            </BannerStyle>
        </StyledWrap>
    )
}
export default Banner;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
`
const BannerStyle = styled.div`
    display: inline-block;
    width: 100%;
    height: 10rem;
    background: url(https://source.unsplash.com/random/1920x1080);
    background-size: cover;
    color: #efefef;
`
const Blank = styled.div`
    min-height: 3rem;
`