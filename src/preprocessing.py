import cv2
import os
import matplotlib.pyplot as plt


def clahe_processing(image_path, output_path, comparison_path):
    if not os.path.exists(image_path):
        return

    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return

    gray_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray_img)

    cv2.imwrite(output_path, clahe_img)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    plt.title("1. Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(gray_img, cmap="gray")
    plt.title("2. Grayscale Simplu")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(clahe_img, cmap="gray")
    plt.title("3. Enhanced (CLAHE)")
    plt.axis("off")

    plt.tight_layout()
    plt.savefig(comparison_path, dpi=150)
    plt.close()

    img_comparatie = cv2.imread(comparison_path)
    if img_comparatie is not None:
        cv2.imshow("Comparatie Rezultat", img_comparatie)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    folder_curent = os.path.dirname(os.path.abspath(__file__))
    folder_proiect = os.path.dirname(folder_curent)

    cale_intrare = os.path.join(folder_proiect, "test_images", "original.jpg")
    cale_iesire = os.path.join(folder_proiect, "test_images", "panou_clahe.jpg")
    cale_comparatie = os.path.join(folder_proiect, "test_images", "comparatie_rezultat.png")

    clahe_processing(cale_intrare, cale_iesire, cale_comparatie)