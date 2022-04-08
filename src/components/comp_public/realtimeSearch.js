//실시간 검색어 기능 해당 기능은 더미데이터론 추축이 불가함 (db에서 최근검색을 추적해야 하는걸로 구상함)
import React from "react";
import styled from "styled-components";


const RealTimeSearch = () => {
    return(
        <StyledWrap>
            <p>검색결과 출력입니다 map함수를 써야할것 같습니다</p>
        </StyledWrap>
    )
}
export default RealTimeSearch;

const StyledWrap = styled.div`
    box-sizing: border-box;
    max-width: 50rem;
    min-width: 18.75rem;
    width: 80%;
    height: 100%;
    margin: 0 auto;
`