
public class ShopItem {
    private String name;
    private int originalPrice;
    private int discountPrice = 0;
    private int weight;

    public ShopItem(String name, int originalPrice, int weight) {
        this.name = name;
        this.originalPrice = originalPrice;
        this.weight = weight;
    }

    public ShopItem(String name, int originalPrice, int discountPrice, int weight) {
        this(name, originalPrice, weight);
        this.discountPrice = discountPrice;
    }
    
    public int getDiscountPrice() {
        return discountPrice;
    }

    public int getOriginalPrice() {
        return originalPrice;
    }

    public String getName() {
        return name;
    }
    @Override
    public String toString() {
        String shopitem = "";
        if (this.discountPrice != 0) {
            shopitem += "Name: " + this.name + ", Original Price: Rs. " + this.originalPrice + ", Discount Price: Rs. "
                    + this.discountPrice + ", Weight: " + this.weight + "g";
        } else {
            shopitem += "Name: " + this.name + ", Original Price: Rs. " + this.originalPrice + ", Weight: " + this.weight + "g";
        }
        return shopitem;
    }
}