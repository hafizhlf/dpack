/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { isBarcodeScannerSupported, scanBarcode } from "@web/webclient/barcode/barcode_scanner";
import { _t } from "@web/core/l10n/translation";

export class BarcodeScannerWidget extends Component {
    static template = "dragon_custom.BarcodeScannerWidget";

    setup() {
        this.notification = useService("notification");
        this.orm = useService("orm");
        this.model = this.props.record.model;
        this.isBarcodeScannerSupported = isBarcodeScannerSupported();
    }

    async handleClick() {
        let error = null;
        let barcode = null;
        try {
            barcode = await scanBarcode(this.env, this.facingMode);
        } catch (err) {
            error = err.message;
        }

        if (barcode) {
            try {
                const result = await this.orm.searchRead("product.product", [
                    ["barcode", "=", barcode],
                ], ["display_name"], { limit: 1 });

                if (result.length > 0) {
                    const product = result[0];
                    this.props.record.update({ product_id: [product.id, product.display_name] });
                } else {
                    this.notification.add(_t("Product not found for scanned barcode."), {
                        type: "warning",
                    });
                }
            } catch (e) {
                this.notification.add(_t("Failed to search product."), {
                    type: "danger",
                });
            }
        } else {
            this.notification.add(error || _t("Please, Scan again!"), {
                type: "warning",
            });
        }
    }
}

registry.category("fields").add("dr_barcode_scanner", {
    component: BarcodeScannerWidget,
});
