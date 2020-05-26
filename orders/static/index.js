document.addEventListener('DOMContentLoaded', () => {

    document.querySelectorAll("p").forEach(p => {
        p.onclick = () => {
            const x = p.parentElement.lastElementChild
            if (x.style.display == "block") {
                x.style.display = "none";
            } else {
                x.style.display = "block";
            }
        }
    });

    if (document.querySelector("select") != null) {
        document.querySelector("select").onchange = () => {
            document.querySelectorAll("a").forEach(a => {
                if (a.getAttribute("data-itemType") == document.querySelector("select").value) {
                    a.style.display = "block";
                } else {
                    a.style.display = "none";
                }
            });
        };
    }

    if (document.getElementById("Yes") != null) {
        document.getElementById("Yes").onclick = () => {
            document.getElementById("selected_toppings").style.display = "block"
        };
    }

    const allowed_toppings = document.querySelector("span").getAttribute("data-numToppings");

    function getSelectValues(select) {
        var result = "";
        var options = select && select.options;
        var opt;
      
        for (var i=0, iLen=options.length; i<iLen; i++) {
          opt = options[i];
      
          if (opt.selected) {
            result = result + (opt.value || opt.text);
          }
        }
        return result;
    }

    document.getElementById("topping_checker").onclick = () => {
        if (allowed_toppings == 0) {
            document.getElementById("real_submit").click();
        }
        else if (getSelectValues(document.getElementById("selected_toppings")).length > allowed_toppings) {
            document.getElementById("error").innerHTML = "You've selected too many toppings.";
        } else {
            const x = getSelectValues(document.getElementById("selected_toppings"));
            document.getElementById("to_change").value = x;
            document.getElementById("real_submit").click();
        }
    }
    /* document.querySelectorAll("a").forEach(a => {
        a.onclick = () => {
            const y = a.getAttribute("data-value");
            const z = document.getElementById(y)
            if (z.style.display == "block") {
                z.style.display = "none";
            } else {
                z.style.display = "block";
            }    
        }
    }); */
});