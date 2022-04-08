import Layout from "../_layout/layout";
import SearchLayout from "../_layout/searchlayout";
import styled from "styled-components";
import HomeMain from "../components/home/homeMain";
import Banner from "../components/comp_public/banner";
import Section1 from "../components/onepage/section1";
import Section2 from "../components/onepage/section2";
import Section3 from "../components/onepage/section3";
import Section4 from "../components/onepage/section4";
import Section7 from "../components/onepage/section7";
import Section8 from "../components/onepage/section8";

const Home = () => {
    return (
        <Layout>

            <Section1/>
            <HomeMain/>
            <Banner/>
            <Section2/>
            <Section3/>
            <Section4/>
            <Section7/>
            <Section8/>

        </Layout>
    )
}
export default Home;

const Blank = styled.div`
    min-height: 1rem;
    `
    //이미지 위치는 public/img /루트가 public폴더