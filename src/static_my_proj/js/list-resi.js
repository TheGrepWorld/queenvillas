$(document).ready(function () {
    let searchParams = new URLSearchParams(window.location.search)
    var is_bed = searchParams.has('bedrooms')
    var is_price = searchParams.has('price')
    // console.log("url: ", is_p)
    if (is_bed === true && is_price === false) {
        var bedrooms = searchParams.get('bedrooms')
        console.log("you selected", bedrooms, "bhk")
        var bed_text = "Showing results for " + bedrooms + " bhk properties"
        document.getElementById("filter-section").innerHTML = bed_text
    }
    if (is_bed === false && is_price === true) {
        var price = searchParams.get('price')
        var price_text = ""
        if (price === '3000000') {
            price_text = "Showing results for " + "Less Than &#8377; 30,00,000" + " price range"
        } else if (price === '5000000') {
            price_text = "Showing results for " + "&#8377; 30,00,000 - &#8377; 50,00,000" + " price range"
        } else if (price === '10000000') {
            price_text = "Showing results for " + "&#8377; 50,00,000 - &#8377; 1,00,00,000" + " price range"
        } else if (price === '100000001') {
            price_text = "Showing results for " + "More than &#8377; 1,00,00,000" + " price range"
        }
        document.getElementById("filter-section").innerHTML = price_text
    }
    if (!(is_bed === true && is_price === true)) {
        return;
    }
    var price = searchParams.get('price')
    var bedrooms = searchParams.get('bedrooms')
    var mix_text = ""
    if (price === '3000000') {
        mix_text = "Showing results for " + bedrooms + " bhk properties in price range Less Than &#8377; 30,00,000"
    } else if (price === '5000000') {
        mix_text = "Showing results for " + bedrooms + " bhk properties in price range &#8377; 30,00,000 - &#8377; 50,00,000"
    } else if (price === '10000000') {
        mix_text = "Showing results for " + bedrooms + " bhk properties in price range of &#8377; 50,00,000 - &#8377; 1,00,00,000"
    } else if (price === '100000001') {
        mix_text = "Showing results for " + bedrooms + " bhk on price range of More than &#8377; 1,00,00,000"

    }
    document.getElementById("filter-section").innerHTML = mix_text
})