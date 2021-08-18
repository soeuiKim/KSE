<?php
/**
 * Custom functions that act independently of the theme templates
 *
 * Eventually, some of the functionality here could be replaced by core features
 *
 * @package unite
 */

/**
 * Get our wp_nav_menu() fallback, wp_page_menu(), to show a home link.
 *
 * @param array $args Configuration arguments.
 * @return array
 */
function unite_page_menu_args( $args ) {
  $args['show_home'] = true;
  return $args;
}
add_filter( 'wp_page_menu_args', 'unite_page_menu_args' );

/**
 * Adds custom classes to the array of body classes.
 *
 * @param array $classes Classes for the body element.
 * @return array
 */
function unite_body_classes( $classes ) {
  // Adds a class of group-blog to blogs with more than 1 published author.
  if ( is_multi_author() ) {
    $classes[] = 'group-blog';
  }

  return $classes;
}
add_filter( 'body_class', 'unite_body_classes' );


// Mark Posts/Pages as Untiled when no title is used
add_filter( 'the_title', 'unite_title' );

function unite_title( $title ) {
  if ( $title == '' ) {
    return esc_html__( 'Untitled', 'unite' );
  } else {
    return $title;
  }
}

/**
 * Allow shortcodes in Dynamic Sidebar
 */
add_filter('widget_text', 'do_shortcode');

/**
 * Prevent page scroll when clicking the more link
 */
function unite_remove_more_link_scroll( $link ) {
  $link = preg_replace( '|#more-[0-9]+|', '', $link );
  return $link;
}
add_filter( 'the_content_more_link', 'unite_remove_more_link_scroll' );

/**
 * Change default "Read More" button when using the_excerpt
 */
function unite_excerpt_more( $more ) {
  return ' <a class="more-link" href="'. esc_url(get_permalink( get_the_ID() )) . '">' . esc_html__( 'Continue reading', 'unite' ) . ' <i class="fa fa-chevron-right"></i></a>';
}
add_filter( 'excerpt_more', 'unite_excerpt_more' );

/**
 * Add Bootstrap classes for table
 */
function unite_add_custom_table_class( $content ) {
    return str_replace( '<table>', '<table class="table table-hover">', $content );
}
add_filter( 'the_content', 'unite_add_custom_table_class' );


if ( ! function_exists( 'custom_password_form' ) ) :
/**
 * password protected post form
 */
function custom_password_form() {
  global $post;
  $label = 'pwbox-'.( empty( $post->ID ) ? rand() : $post->ID );
  $o = '<form class="protected-post-form" action="' . get_option('siteurl') . '/wp-login.php?action=postpass" method="post">
        <div class="row">
          <div class="col-lg-10">
              ' . __( "<p>This post is password protected. To view it please enter your password below:</p>" ,'unite') . '
              <label for="' . $label . '">' . __( "Password:" ,'unite') . ' </label>
            <div class="input-group">
              <input class="form-control" value="' . get_search_query() . '" name="post_password" id="' . $label . '" type="password">
              <span class="input-group-btn"><button type="submit" class="btn btn-primary" name="submit" id="searchsubmit" vvalue="' . esc_attr__( "Submit",'unite' ) . '">' . __( "Submit" ,'unite') . '</button>
              </span>
            </div>
          </div>
        </div>
      </form>';
  return $o;
}
endif;
add_filter( 'the_password_form', 'custom_password_form' );


if ( ! function_exists( 'unite_social' ) ) :
/**
 * Process social links from Theme Options
 */
function unite_social(){
  $output = '<div id="social" class="social">';
  $output .= unite_social_item(unite_get_option('social_facebook'), 'Facebook', 'facebook');
  $output .= unite_social_item(unite_get_option('social_twitter'), 'Twitter', 'twitter');
  // Google plus discontinued
  //$output .= unite_social_item(unite_get_option('social_google'), 'Google Plus', 'google-plus');
  $output .= unite_social_item(unite_get_option('social_youtube'), 'YouTube', 'youtube');
  $output .= unite_social_item(unite_get_option('social_linkedin'), 'LinkedIn', 'linkedin');
  $output .= unite_social_item(unite_get_option('social_pinterest'), 'Pinterest', 'pinterest');
  $output .= unite_social_item(unite_get_option('social_feed'), 'Feed', 'rss');
  $output .= unite_social_item(unite_get_option('social_tumblr'), 'Tumblr', 'tumblr');
  $output .= unite_social_item(unite_get_option('social_flickr'), 'Flickr', 'flickr');
  $output .= unite_social_item(unite_get_option('social_instagram'), 'Instagram', 'instagram');
  $output .= unite_social_item(unite_get_option('social_dribbble'), 'Dribbble', 'dribbble');
  $output .= unite_social_item(unite_get_option('social_skype'), 'Skype', 'skype');
  $output .= unite_social_item(unite_get_option('social_vimeo'), 'Vimeo', 'vimeo-square');
  $output .= '</div>';
  echo $output;
}
endif;


if ( ! function_exists( 'unite_social_item' ) ) :
/**
 * Output social links on frontend.
 */
function unite_social_item($url, $title = '', $icon = ''){
  if($url != ''):
    $output = '<a class="social-profile '.$icon.'" href="'.esc_url($url).'" target="_blank" title="'.$title.'">';
    if($icon != '') $output .= '<span class="social_icon fa fa-'.$icon.'"></span>';
    $output .= '</a>';
    return $output;
  endif;
}
endif;


if ( ! function_exists( 'unite_footer_links' ) ) :
/**
 * footer menu (should you choose to use one)
 */
function unite_footer_links() {
  // display the WordPress Custom Menu if available
  wp_nav_menu(array(
    'container'       => '',                              // remove nav container
    'container_class' => 'footer-links clearfix',   // class of container (should you choose to use it)
    'menu'            => __( 'Footer Links', 'unite' ),   // nav name
    'menu_class'      => 'nav footer-nav clearfix',      // adding custom nav class
    'theme_location'  => 'footer-links',             // where it's located in the theme
    'before'          => '',                                 // before the menu
    'after'           => '',                                  // after the menu
    'link_before'     => '',                            // before each link
    'link_after'      => '',                             // after each link
    'depth'           => 0,                                   // limit the depth of the nav
    'fallback_cb'     => 'unite_footer_links_fallback'  // fallback function
  ));
} /* end unite footer link */
endif;
/**
 * function to show the footer info, copyright information
 */
function unite_footer_info() {
   $output = '<a href="http://colorlib.com/wp/unite" title="Unite Theme" target="_blank" rel="nofollow noopener">'.esc_html__('Unite Theme','unite').'</a> '.esc_html__('powered by','unite').' <a href="http://wordpress.org" title="WordPress" target="_blank">WordPress</a>.';
   echo $output;
}
add_action( 'unite_footer', 'unite_footer_info', 30 );


if ( ! function_exists( 'get_unite_theme_options' ) )  {
/**
 * Generate custom CSS output in website source from Theme Options.
 */
    function get_unite_theme_options(){

      echo '<style type="text/css">';

      if ( unite_get_option('link_color')) {
        echo 'a, #infinite-handle span {color:' . unite_get_option('link_color') . '}';
      }
      if ( unite_get_option('link_hover_color')) {
        echo 'a:hover, a:focus {color: '.unite_get_option('link_hover_color', '#000').';}';
      }
      if ( unite_get_option('link_active_color')) {
        echo 'a:active {color: '.unite_get_option('link_active_color', '#000').';}';
      }
      if ( unite_get_option('element_color')) {
        echo '.btn-primary, .label-primary, .carousel-caption h4 {background-color: '.unite_get_option('element_color', '#000').'; border-color: '.unite_get_option('element_color', '#000').';} hr.section-divider:after, .entry-meta .fa { color: '.unite_get_option('element_color', '#000').'}';
      }
      if ( unite_get_option('element_color_hover')) {
		echo '.label-primary[href]:hover, .label-primary[href]:focus, #infinite-handle span:hover, #infinite-handle span:focus-within, .btn.btn-primary.read-more:hover, .btn.btn-primary.read-more:focus, .btn-primary:hover, .btn-primary:focus, .btn-primary:active, .btn-primary.active, .site-main [class*="navigation"] a:hover, .site-main [class*="navigation"] a:focus, .more-link:hover, .more-link:focus, #image-navigation .nav-previous a:hover, #image-navigation .nav-previous a:focus, #image-navigation .nav-next a:hover, #image-navigation .nav-next a:focus { background-color: '.unite_get_option('element_color_hover', '#000').'; border-color: '.unite_get_option('element_color_hover', '#000').'; }';
      }
      if ( unite_get_option('heading_color')) {
        echo 'h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6, .entry-title {color: '.unite_get_option('heading_color', '#000').';}';
      }
      if ( unite_get_option('top_nav_bg_color')) {
        echo '.navbar.navbar-default {background-color: '.unite_get_option('top_nav_bg_color', '#000').';}';
      }
      if ( unite_get_option('top_nav_link_color')) {
        echo '.navbar-default .navbar-nav > li > a, .navbar-default .navbar-nav > .open > a, .navbar-default .navbar-nav > .open > a:hover, .navbar-default .navbar-nav > .open > a:focus, .navbar-default .navbar-nav > .active > a, .navbar-default .navbar-nav > .active > a:hover, .navbar-default .navbar-nav > .active > a:focus { color: '.unite_get_option('top_nav_link_color', '#000').';}';
      }
      if ( unite_get_option('top_nav_dropdown_bg')) {
        echo '.dropdown-menu, .dropdown-menu > .active > a, .dropdown-menu > .active > a:hover, .dropdown-menu > .active > a:focus {background-color: '.unite_get_option('top_nav_dropdown_bg', '#000').';}';
      }
      if ( unite_get_option('top_nav_dropdown_item')) {
        echo '.navbar-default .navbar-nav .open .dropdown-menu > li > a { color: '.unite_get_option('top_nav_dropdown_item', '#000').';}';
      }
      if ( unite_get_option('footer_bg_color')) {
        echo '#colophon {background-color: '.unite_get_option('footer_bg_color', '#000').';}';
      }
      if ( unite_get_option('footer_text_color')) {
        echo '.copyright {color: '.unite_get_option('footer_text_color', '#000').';}';
      }
      if ( unite_get_option('footer_link_color')) {
        echo '.site-info a {color: '.unite_get_option('footer_link_color', '#000').';}';
      }
      if ( unite_get_option('social_color')) {
        echo '.social-icons li a {color: '.unite_get_option('social_color', '#000').' !important;}';
      }
      $typography = unite_get_option('main_body_typography');
      if ( $typography ) {
        echo '.entry-content {font-family: ' . $typography['face'] . '; font-size:' . $typography['size'] . '; font-weight: ' . $typography['style'] . '; color:'.$typography['color'] . ';}';
      }
      if ( unite_get_option('custom_css')) {
        echo html_entity_decode( unite_get_option( 'custom_css', 'no entry' ) );
      }
        echo '</style>';
    }
}
add_action('wp_head','get_unite_theme_options',10);

/**
 *  Theme Options sidebar
 */
add_action( 'optionsframework_after','unite_options_display_sidebar' );

function unite_options_display_sidebar() { ?>

  <div id="optionsframework-sidebar" class="metabox-holder">
    <div id="optionsframework" class="postbox">
        <h3><?php _e('Support and Documentation','unite') ?></h3>
          <div class="inside">
              <div id="social-share">
                <div class="fb-like" data-href="https://www.facebook.com/colorlib" data-send="false" data-layout="button_count" data-width="90" data-show-faces="true"></div>
                <div class="tw-follow" ><a href="https://twitter.com/colorlib" class="twitter-follow-button" data-show-count="false"><?php esc_html_e('Follow','unite'); ?> @colorlib</a></div>
              </div>
                <p><b><a href="http://colorlib.com/wp/support/unite"><?php _e('Unite Documentation','unite'); ?></a></b></p>
                <p><?php _e('The best way to contact us with <b>support questions</b> and <b>bug reports</b> is via','unite') ?> <a href="http://colorlib.com/wp/forums"><?php _e('Colorlib support forum','unite') ?></a>.</p>
                <p><?php _e('If you like this theme, I\'d appreciate any of the following:','unite') ?></p>
                <ul>
                    <li><a class="button" href="http://wordpress.org/support/view/theme-reviews/unite?filter=5" title="<?php esc_attr_e('Rate this Theme', 'unite'); ?>" target="_blank"><?php printf(__('Rate this Theme','unite')); ?></a></li>
                    <li><a class="button" href="http://www.facebook.com/colorlib" title="<?php esc_attr_e('Like Colorlib on Facebook','unite'); ?>" target="_blank"><?php printf(__('Like on Facebook','unite')); ?></a></li>
                    <li><a class="button" href="http://twitter.com/colorlib/" title="<?php esc_attr_e('Follow Colorlib on Twitter','unite'); ?>" target="_blank"><?php printf(__('Follow on Twitter','unite')); ?></a></li>
                </ul>
          </div>
      </div>
    </div>
<?php }

/*-----------------------------------------------------------------------------------*/
/*  Theme Plugin
/*-----------------------------------------------------------------------------------*/
/**
 * Include the TGM_Plugin_Activation class.
 */
require_once get_template_directory() . '/inc/class-tgm-plugin-activation.php';
add_action( 'tgmpa_register', 'unite_register_required_plugins' );

/**
 * Register the required plugins for this theme.
 *
 * In this example, we register five plugins:
 * - one included with the TGMPA library
 * - two from an external source, one from an arbitrary source, one from a GitHub repository
 * - two from the .org repo, where one demonstrates the use of the `is_callable` argument
 *
 * The variables passed to the `tgmpa()` function should be:
 * - an array of plugin arrays;
 * - optionally a configuration array.
 * If you are not changing anything in the configuration array, you can remove the array and remove the
 * variable from the function call: `tgmpa( $plugins );`.
 * In that case, the TGMPA default settings will be used.
 *
 * This function is hooked into `tgmpa_register`, which is fired on the WP `init` action on priority 10.
 */
function unite_register_required_plugins() {
  /*
   * Array of plugin arrays. Required keys are name and slug.
   * If the source is NOT from the .org repo, then source is also required.
   */
  $plugins = array(

    array(
      'name'    => 'CPT Bootstrap Carousel',
      'slug'    => 'cpt-bootstrap-carousel',
      'required'  => false,
    ),

  );

  /*
   * Array of configuration settings. Amend each line as needed.
   *
   * TGMPA will start providing localized text strings soon. If you already have translations of our standard
   * strings available, please help us make TGMPA even better by giving us access to these translations or by
   * sending in a pull-request with .po file(s) with the translations.
   *
   * Only uncomment the strings in the config array if you want to customize the strings.
   */
  $config = array(
    'id'           => 'unite',                 // Unique ID for hashing notices for multiple instances of TGMPA.
    'default_path' => '',                      // Default absolute path to bundled plugins.
    'menu'         => 'tgmpa-install-plugins', // Menu slug.
    'has_notices'  => true,                    // Show admin notices or not.
    'dismissable'  => true,                    // If false, a user cannot dismiss the nag message.
    'dismiss_msg'  => '',                      // If 'dismissable' is false, this message will be output at top of nag.
    'is_automatic' => false,                   // Automatically activate plugins after installation or not.
    'message'      => '',                      // Message to output right before the plugins table.
  );

  tgmpa( $plugins, $config );
}

/*
 * Basic WooCommerce setup.
 */
add_action('woocommerce_before_main_content', 'unite_wrapper_start', 10);
add_action('woocommerce_after_main_content', 'unite_wrapper_end', 10);

function unite_wrapper_start() {
  echo '<div id="primary" class="col-md-8">';
}

function unite_wrapper_end() {
  echo '</div>';
}


if ( ! function_exists( 'unite_woocommerce_menucart' ) ) :
/**
 * Place a cart icon with number of items and total cost in the menu bar.
 *
 * https://gist.github.com/srikat/8264387#file-functions-php
 */
function unite_woocommerce_menucart($menu, $args) {

  // Check if WooCommerce is active and add a new item to a menu assigned to Primary Navigation Menu location
  if ( !in_array( 'woocommerce/woocommerce.php', apply_filters( 'active_plugins', get_option( 'active_plugins' ) ) ) || 'primary' !== $args->theme_location )
    return $menu;

  ob_start();
    global $woocommerce;
    $viewing_cart = __('View your shopping cart', 'unite');
    $start_shopping = __('Start shopping', 'unite');
    $cart_url = $woocommerce->cart->get_cart_url();
    $shop_page_url = esc_url(get_permalink( woocommerce_get_page_id( 'shop' ) ));
    $cart_contents_count = $woocommerce->cart->cart_contents_count;
    $cart_contents = sprintf(_n('%d item', '%d items', $cart_contents_count, 'unite'), $cart_contents_count);
    $cart_total = $woocommerce->cart->get_cart_total();
    // Uncomment the line below to hide nav menu cart item when there are no items in the cart
    // if ( $cart_contents_count > 0 ) {
      if ($cart_contents_count == 0) {
        $menu_item = '</ul><ul class="nav navbar-nav navbar-right"><li><a class="woomenucart-menu-item" href="'. $shop_page_url .'" title="'. $start_shopping .'">';
      } else {
        $menu_item = '</ul><ul class="nav navbar-nav navbar-right"><li><a class="woomenucart-menu-item" href="'. $cart_url .'" title="'. $viewing_cart .'">';
      }

      $menu_item .= '<i class="fa fa-shopping-cart"></i> ';

      $menu_item .= $cart_contents.' - '. $cart_total;
      $menu_item .= '</a></li></ul>';
    // Uncomment the line below to hide nav menu cart item when there are no items in the cart
    // }
    echo $menu_item;
  $social = ob_get_clean();
  return $menu . $social;

}
endif;
add_filter('wp_nav_menu_items','unite_woocommerce_menucart', 10, 2);

/**
 * Get custom CSS from Theme Options panel and output in header
 */
if (!function_exists('get_unite_theme_options'))  {
  function get_unite_theme_options(){

    echo '<style type="text/css">';

    if ( unite_get_option('link_color')) {
      echo 'a, #infinite-handle span {color:' . unite_get_option('link_color') . '}';
    }
    if ( unite_get_option('link_hover_color')) {
      echo 'a:hover, a:focus {color: '.unite_get_option('link_hover_color', '#000').';}';
    }
    if ( unite_get_option('link_active_color')) {
      echo 'a:active {color: '.unite_get_option('link_active_color', '#000').';}';
    }
    if ( unite_get_option('element_color')) {
      echo '.btn-default, .label-default, .flex-caption h2, .navbar-default .navbar-nav > .active > a, .navbar-default .navbar-nav > .active > a:hover, .navbar-default .navbar-nav > .active > a:focus, .navbar-default .navbar-nav > li > a:hover, .navbar-default .navbar-nav > li > a:focus, .navbar-default .navbar-nav > .open > a, .navbar-default .navbar-nav > .open > a:hover, .navbar-default .navbar-nav > .open > a:focus, .dropdown-menu > li > a:hover, .dropdown-menu > li > a:focus, .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover, .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus, .dropdown-menu > .active > a, .navbar-default .navbar-nav .open .dropdown-menu > .active > a {background-color: '.unite_get_option('element_color', '#000').'; border-color: '.unite_get_option('element_color', '#000').';} .btn.btn-default.read-more, .entry-meta .fa, .site-main [class*="navigation"] a, .more-link { color: '.unite_get_option('element_color', '#000').'}';
    }
    if ( unite_get_option('element_color_hover')) {
	  echo '.label-default[href]:hover, .label-default[href]:focus, #infinite-handle span:hover, #infinite-handle span:focus-within, .btn.btn-default.read-more:hover, .btn.btn-default.read-more:focus, .btn-default:hover, .btn-default:focus, .scroll-to-top:hover, .scroll-to-top:focus, .btn-default:focus, .btn-default:active, .btn-default.active, .site-main [class*="navigation"] a:hover, .site-main [class*="navigation"] a:focus, .more-link:hover, .more-link:focus, #image-navigation .nav-previous a:hover, #image-navigation .nav-previous a:focus, #image-navigation .nav-next a:hover, #image-navigation .nav-next a:focus { background-color: '.unite_get_option('element_color_hover', '#000').'; border-color: '.unite_get_option('element_color_hover', '#000').'; }';
    }
    if ( unite_get_option('cfa_bg_color')) {
      echo '.cfa { background-color: '.unite_get_option('cfa_bg_color', '#000').'; } .cfa-button:hover {color: '.unite_get_option('cfa_bg_color', '#000').';}';
    }
    if ( unite_get_option('cfa_color')) {
      echo '.cfa-text { color: '.unite_get_option('cfa_color', '#000').';}';
    }
    if ( unite_get_option('cfa_btn_color')) {
      echo '.cfa-button {border-color: '.unite_get_option('cfa_btn_color', '#000').';}';
    }
    if ( unite_get_option('cfa_btn_txt_color')) {
      echo '.cfa-button {color: '.unite_get_option('cfa_btn_txt_color', '#000').';}';
    }
    if ( unite_get_option('heading_color')) {
      echo 'h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6, .entry-title {color: '.unite_get_option('heading_color', '#000').';}';
    }
    if ( unite_get_option('top_nav_bg_color')) {
      echo '.navbar.navbar-default {background-color: '.unite_get_option('top_nav_bg_color', '#000').';}';
    }
    if ( unite_get_option('top_nav_link_color')) {
      echo '.navbar-default .navbar-nav > li > a { color: '.unite_get_option('top_nav_link_color', '#000').';}';
    }
    if ( unite_get_option('top_nav_dropdown_bg')) {
      echo '.dropdown-menu, .dropdown-menu > .active > a, .dropdown-menu > .active > a:hover, .dropdown-menu > .active > a:focus {background-color: '.unite_get_option('top_nav_dropdown_bg', '#000').';}';
    }
    if ( unite_get_option('top_nav_dropdown_item')) {
      echo '.navbar-default .navbar-nav .open .dropdown-menu > li > a { color: '.unite_get_option('top_nav_dropdown_item', '#000').';}';
    }
    if ( unite_get_option('footer_bg_color')) {
      echo '#colophon {background-color: '.unite_get_option('footer_bg_color', '#000').';}';
    }
    if ( unite_get_option('footer_text_color')) {
      echo '#footer-area, .site-info {color: '.unite_get_option('footer_text_color', '#000').';}';
    }
    if ( unite_get_option('footer_widget_bg_color')) {
      echo '#footer-area {background-color: '.unite_get_option('footer_widget_bg_color', '#000').';}';
    }
    if ( unite_get_option('footer_link_color')) {
      echo '.site-info a, #footer-area a {color: '.unite_get_option('footer_link_color', '#000').';}';
    }
    if ( unite_get_option('social_color')) {
      echo '.social-icons ul a {color: '.unite_get_option('social_color', '#000').' !important ;}';
    }
    $typography_options = Unite_Helper::get_typography_options();
    $typography = unite_get_option('main_body_typography');
    if ( $typography ) {
      echo '.entry-content {font-family: ' . $typography_options['faces'][$typography['face']] . '; font-size:' . $typography['size'] . '; font-weight: ' . $typography['style'] . '; color:'.$typography['color'] . ';}';
    }
    if ( unite_get_option('custom_css')) {
      echo html_entity_decode( unite_get_option( 'custom_css', 'no entry' ) );
    }
      echo '</style>';
  }
}
add_action('wp_head','get_unite_theme_options',10);


/**
 * Allows users to save skype protocol skype: in menu URL
 */
function unite_allow_skype_protocol( $protocols ){
    $protocols[] = 'skype';
    return $protocols;
}
add_filter( 'kses_allowed_protocols' , 'unite_allow_skype_protocol' );

?>
