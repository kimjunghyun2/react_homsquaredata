//광고 배너 기능에 해당 단 img는 그때 그때 달라질 수 있음 
import React from "react";
import styled from "styled-components";


const SideBanner = () => {
    return(
        <StyledWrap>
            <BannerStyle>
            <p>사이드 배너입니다. 실사용시에는 없어야 합니다 swipper로 구현할 수도 있습니다.</p>
            </BannerStyle>
            <Blank/>
            
        </StyledWrap>
    )
}
export default SideBanner;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 15rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
    float: right;
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