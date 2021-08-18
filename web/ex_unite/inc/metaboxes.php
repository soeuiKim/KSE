<?php
/**
 * Unite Meta Boxes
 *
 */

add_action('add_meta_boxes', 'unite_add_custom_box');
/**
 * Add Meta Boxes.
 *
 * Add Meta box in page and post post types.
 */
function unite_add_custom_box()
{
    add_meta_box('siderbar-layout', //Unique ID
        __('Select layout for this specific Page only ( Note: This setting only reflects if page Template is set as Default Template and Blog Type Templates.)', 'unite'), //Title
        'unite_sidebar_layout', //Callback function
        'page' //show metabox in pages
        );
    add_meta_box('siderbar-layout', //Unique ID
        __('Select layout for this specific Post only', 'unite'), //Title
        'unite_sidebar_layout', //Callback function
        'post', //show metabox in posts
        'side'
        );
}

/**
 * Displays metabox to for sidebar layout
 */
function unite_sidebar_layout()
{
    global $post;
    $site_layout = Unite_Helper::get_site_layout();
    // Use nonce for verification
    wp_nonce_field(basename(__FILE__), 'custom_meta_box_nonce'); ?>
	
    <table id="sidebar-metabox" class="form-table" width="100%">
        <tbody>
            <tr>
                <label class="description"><?php
                    $layout = get_post_meta($post->ID, 'site_layout', true);?>                        
                    <select name="site_layout" id="site_layout">
                        <option value=""><?php esc_html_e( 'Default', 'unite' ); ?></option>
                        <?php foreach( $site_layout as $key=>$val ) { ?>
                        <option value="<?php echo esc_attr($key); ?>" <?php selected( $layout, $key ); ?> ><?php echo esc_html($val); ?></option>
                        <?php } ?>
                    </select>                           
                </label>
            </tr>
        </tbody>
    </table><?php
}

/****************************************************************************************/


add_action('save_post', 'unite_save_custom_meta');
/**
 * save the custom metabox data
 * @hooked to save_post hook
 */
function unite_save_custom_meta($post_id)
{
    global $post;
    $site_layout = Unite_Helper::get_site_layout();
    
    // Verify the nonce before proceeding.
    if (!isset($_POST['custom_meta_box_nonce']) || !wp_verify_nonce($_POST['custom_meta_box_nonce'], basename(__FILE__)))
        return;
    
    // Stop WP from clearing custom fields on autosave
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE)
        return;
    
    if ('page' == $_POST['post_type']) {
        if (!current_user_can('edit_page', $post_id))
            return $post_id;
    } elseif (!current_user_can('edit_post', $post_id)) {
        return $post_id;
    }

    if ( $_POST['site_layout'] ) {
        $layout = isset( $site_layout[ $_POST['site_layout'] ] ) ? $_POST['site_layout'] : 'side-pull-left';
        update_post_meta( $post_id, 'site_layout', $layout );
    } else{
        delete_post_meta( $post_id, 'site_layout' );
    }
}