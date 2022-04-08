import Layout from "../_layout/layout";
import SearchLayout from "../_layout/searchlayout";
import Banner from "../components/comp_public/banner";
import SearchResultMain from "../components/search_result/SearchResultMain";

const SearchResult = () => {
    return (
        <Layout>
            <SearchResultMain/>
            <Banner/>
        </Layout>
    )
}
export default SearchResult;